# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock, call, patch

import numpy as np
import pandas as pd

from btb.tuning.hyperparams.categorical import CategoricalHyperParam
from btb.tuning.tunable import Tunable


def assert_called_with_np_array(mock_calls, real_calls):
    assert len(mock_calls) == len(real_calls)

    for mock_call, real_call in zip(mock_calls, real_calls):
        np.testing.assert_array_equal(mock_call[0], real_call[1])


class TestTunable(TestCase):
    """Unit test for the class ``Tunable``."""

    def setUp(self):
        """Instantiate the ``Tunable`` and it's ``Hyperparameters`` that we will be using."""
        self.bhp = MagicMock()
        self.chp = MagicMock()
        self.ihp = MagicMock()

        hyperparams = {
            'bhp': self.bhp,
            'chp': self.chp,
            'ihp': self.ihp,
        }

        self.instance = Tunable(hyperparams, names=['bhp', 'chp', 'ihp'])

    @patch('btb.tuning.tunable.list')
    def test___init__not_given_names(self, list_mock):
        """Test the init method without giving names to it."""

        # A mock for list() is being used as python 3.5 does not maintain the order.
        # setup
        list_mock.return_value = ['a', 'b']

        # run
        self.instance = Tunable({'a': 1, 'b': 2})

        # assert
        list_mock.assert_called_once_with({'a': 1, 'b': 2})
        assert self.instance.names == ['a', 'b']

    def test___init__with_given_names(self):
        """Test that the names are being generated correctly."""

        # run
        instance = Tunable({}, names=['bhp', 'chp', 'ihp'])

        # assert
        assert instance.names == ['bhp', 'chp', 'ihp']

    def test_transform_valid_dict(self):
        """Test transform method with a dictionary that has all the hyperparameters."""
        # setup
        self.bhp.transform.return_value = [[1]]
        self.chp.transform.return_value = [[0]]
        self.ihp.transform.return_value = [[1]]

        values_dict = {
            'bhp': True,
            'chp': 'cat',
            'ihp': 1
        }

        # run
        result = self.instance.transform(values_dict)

        # assert
        self.bhp.transform.assert_called_once_with(True)
        self.chp.transform.assert_called_once_with('cat')
        self.ihp.transform.assert_called_once_with(1)

        np.testing.assert_array_equal(result, np.array([[1, 0, 1]]))

    def test_transform_empty_dict(self):
        """Test transform method with a dictionary that has a missing hyperparameters."""
        # run / assert
        with self.assertRaises(KeyError):
            self.instance.transform({})

    def test_transform_invalid_dict_one_missing(self):
        """Test transform method with a dictionary that has a missing hyperparameters."""
        # run / assert
        values = {
            'bhp': True,
            'chp': 'cat'
        }

        with self.assertRaises(KeyError):
            self.instance.transform(values)

    def test_transform_list_of_dicts(self):
        """Test transform method with a list of dictionaries."""
        # setup
        self.bhp.transform.return_value = [[1], [0]]
        self.chp.transform.return_value = [[0], [1]]
        self.ihp.transform.return_value = [[1], [1]]

        values_list_dict = [
            {'bhp': True, 'chp': 'cat', 'ihp': 2},
            {'bhp': False, 'chp': 'cat', 'ihp': 3}
        ]

        # run
        results = self.instance.transform(values_list_dict)

        # assert
        assert_called_with_np_array(self.bhp.transform.call_args_list, [call([True, False])])
        assert_called_with_np_array(self.chp.transform.call_args_list, [call(['cat', 'cat'])])
        assert_called_with_np_array(self.ihp.transform.call_args_list, [call([2, 3])])

        np.testing.assert_array_equal(results, np.array([[1, 0, 1], [0, 1, 1]]))

    def test_transform_list_of_invalid_dicts(self):
        """Test transform method with a list of dictionaries where one of them does not have
        the categorical value."""

        # setup
        self.bhp.transform.return_value = [[1], [0]]

        # Here we create a CHP so we can raise an value error as there will be a NaN inside the
        # pandas.DataFrame.
        self.chp = CategoricalHyperParam(['cat', 'dog'])
        self.ihp.transform.return_value = [[1], [1]]

        values_list_dict = [
            {'bhp': True, 'ihp': 2},
            {'bhp': False, 'chp': 'cat', 'ihp': 3}
        ]

        # run / assert
        with self.assertRaises(ValueError):
            self.instance.transform(values_list_dict)

    def test_transform_empty_list(self):
        """Test transform method with an empty list."""
        # run / assert
        with self.assertRaises(IndexError):
            self.instance.transform(list())

    def test_transform_valid_pandas_series(self):
        """Test transform method over a valid ``pandas.Series`` object."""
        # setup
        self.bhp.transform.return_value = [[1]]
        self.chp.transform.return_value = [[0]]
        self.ihp.transform.return_value = [[1]]

        values = pd.Series([False, 'cat', 1], index=['bhp', 'chp', 'ihp'])

        # run
        result = self.instance.transform(values)

        # assert
        self.bhp.transform.assert_called_once_with(False)
        self.chp.transform.assert_called_once_with('cat')
        self.ihp.transform.assert_called_once_with(1)

        np.testing.assert_array_equal(result, np.array([[1, 0, 1]]))

    def test_transform_invalid_pandas_series(self):
        """Test transform method over a ``pandas.Series`` object that does not have index."""
        # setup
        values = pd.Series([False, 'cat', 1])

        # run
        with self.assertRaises(KeyError):
            self.instance.transform(values)

    def test_transform_array_like_list(self):
        """Test transform a valid array like list."""
        # setup
        self.bhp.transform.return_value = [[1]]
        self.chp.transform.return_value = [[0]]
        self.ihp.transform.return_value = [[1]]

        values = [[True, 'dog', 2], [False, 'cat', 3]]

        # run
        result = self.instance.transform(values)

        # assert
        assert_called_with_np_array(
            self.bhp.transform.call_args_list,
            [call(np.array([True, False]))]
        )
        assert_called_with_np_array(
            self.chp.transform.call_args_list,
            [call(np.array(['dog', 'cat']))]
        )
        assert_called_with_np_array(
            self.ihp.transform.call_args_list,
            [call(np.array([2, 3]))]
        )

        np.testing.assert_array_equal(result, np.array([[1, 0, 1]]))

    def test_transform_simple_list(self):
        """Test that the method transform performs a transformation over a list with a single
        combination of hyperparameter valid values.
        """
        # setup
        self.bhp.transform.return_value = [[1]]
        self.chp.transform.return_value = [[0]]
        self.ihp.transform.return_value = [[1]]

        values = [True, 'dog', 2]

        # run
        result = self.instance.transform(values)

        # assert
        self.bhp.transform.assert_called_once_with(True)
        self.chp.transform.assert_called_once_with('dog')
        self.ihp.transform.assert_called_once_with(2)

        np.testing.assert_array_equal(result, np.array([[1, 0, 1]]))

    def test_transform_pd_df(self):
        """Test that the method transform performs a transformation over a ``pandas.DataFrame``
        with a single combination of hyperparameter valid values.
        """
        # setup
        self.bhp.transform.return_value = [[1]]
        self.chp.transform.return_value = [[0]]
        self.ihp.transform.return_value = [[1]]

        values = pd.DataFrame([[True, 'dog', 2]], columns=['bhp', 'chp', 'ihp'])

        # run
        result = self.instance.transform(values)

        # assert
        self.bhp.transform.assert_called_once_with(True)
        self.chp.transform.assert_called_once_with('dog')
        self.ihp.transform.assert_called_once_with(2)

        np.testing.assert_array_equal(result, np.array([[1, 0, 1]]))

    def test_transform_simple_invalid_list(self):
        """Test that the method transform does not transform a list with a single combination
        of invalid hyperparameter values.
        """
        # run / assert
        with self.assertRaises(TypeError):
            self.instance.transform([[True], 1, 2])

    def test_inverse_transform_valid_data(self):
        """Test that the inverse transform method is calling the hyperparameters."""
        # setup
        self.bhp.K = 1
        self.chp.K = 1
        self.ihp.K = 1

        self.bhp.inverse_transform.return_value = [[True]]
        self.chp.inverse_transform.return_value = [['cat']]
        self.ihp.inverse_transform.return_value = [[1]]

        values = [[1, 0, 1]]

        # run
        result = self.instance.inverse_transform(values)

        # assert
        expected_result = pd.DataFrame(
            {
                'bhp': [True],
                'chp': ['cat'],
                'ihp': [1]
            },
            dtype=object
        )

        self.bhp.inverse_transform.assert_called_once_with([1])
        self.chp.inverse_transform.assert_called_once_with([0])
        self.ihp.inverse_transform.assert_called_once_with([1])
        pd.testing.assert_frame_equal(result, expected_result)

    def test_inverse_transform_invalid_data(self):
        """Test that the a ``TypeError`` is being raised when calling with the invalid data."""
        # setup
        values = [1, 0, 1]

        # run
        with self.assertRaises(TypeError):
            self.instance.inverse_transform(values)

    def test_sample(self):
        """Test that the method sample generates data from all the ``hyperparams``."""

        # setup
        # Values have been changed to ensure that each one of them is being called.
        self.bhp.sample.return_value = [[True]]
        self.chp.sample.return_value = [['dog']]
        self.ihp.sample.return_value = [[4]]

        # run
        result = self.instance.sample(1)

        # assert
        expected_result = [[True, 'dog', 4]]

        self.bhp.sample.assert_called_once_with(1)
        self.chp.sample.assert_called_once_with(1)
        self.ihp.sample.assert_called_once_with(1)
        assert (result == expected_result).all()
