# -*- coding: utf-8 -*-

"""
Datasets module.

This module contains collections of datsets from our ``S3``
https://atm-data.s3.amazonaws.com . There is also a function
that filters over this collections and returns the requested
one as a copy.
"""

# Available datasets sorted by execution time, slowest first
ALL_DATASETS_BY_TIME = [
    'BNG(cmc)_1.csv',
    'eye_movements_1.csv',
    'wall-robot-navigation_1.csv',
    'analcatdata_germangss_2.csv',
    'scene_1.csv',
    'arcene_1.csv',
    'mv_1.csv',
    'bank32nh_1.csv',
    'BNG(cmc,nominal,55296)_1.csv',
    'AP_Endometrium_Prostate_1.csv',
    'house_16H_1.csv',
    'waveform-5000_1.csv',
    'autoUniv-au4-2500_1.csv',
    'BNG(breast-w)_1.csv',
    'wall-robot-navigation_2.csv',
    'madelon_1.csv',
    'Click_prediction_small_1.csv',
    'wall-robot-navigation_3.csv',
    'nursery_1.csv',
    'kdd_JapaneseVowels_1.csv',
    'house_8L_1.csv',
    'MagicTelescope_1.csv',
    'vehicle_1.csv',
    'musk_1.csv',
    'BNG(vote)_1.csv',
    'PopularKids_1.csv',
    'abalone_2.csv',
    'rmftsa_sleepdata_2.csv',
    'yeast_ml8_1.csv',
    'leukemia_1.csv',
    'electricity_1.csv',
    'CreditCardSubset_1.csv',
    'cmc_1.csv',
    'car_1.csv',
    'autoUniv-au7-700_1.csv',
    'grub-damage_1.csv',
    'analcatdata_authorship_1.csv',
    'skin-segmentation_1.csv',
    'splice_1.csv',
    'cpu_small_1.csv',
    'tumors_C_1.csv',
    'cpu_act_1.csv',
    'ringnorm_1.csv',
    'bank-marketing_2.csv',
    'mfeat-factors_1.csv',
    'pol_1.csv',
    '2dplanes_1.csv',
    'Amazon_employee_access_1.csv',
    'cal_housing_1.csv',
    'houses_1.csv',
    'BNG(tic-tac-toe)_1.csv',
    'mozilla4_1.csv',
    'cardiotocography_1.csv',
    'meta_ensembles.arff_1.csv',
    'balance-scale_1.csv',
    'fried_1.csv',
    'tae_1.csv',
    'spambase_1.csv',
    'ozone-level-8hr_1.csv',
    'PhishingWebsites_1.csv',
    'elevators_1.csv',
    'bank8FM_1.csv',
    'mammography_1.csv',
    'hayes-roth_2.csv',
    'sylva_prior_1.csv',
    'meta_batchincremental.arff_1.csv',
    'waveform-5000_2.csv',
    'teachingAssistant_1.csv',
    'ailerons_1.csv',
    'robot-failures-lp1_1.csv',
    'desharnais_1.csv',
    'PieChart4_1.csv',
    'eeg-eye-state_1.csv',
    'Engine1_1.csv',
    'puma32H_1.csv',
    'lymph_1.csv',
    'wind_1.csv',
    'mfeat-fourier_1.csv',
    'steel-plates-fault_1.csv',
    'mfeat-karhunen_1.csv',
    'meta_instanceincremental.arff_1.csv',
    'page-blocks_1.csv',
    'twonorm_1.csv',
    'mc1_1.csv',
    'wine_1.csv',
    'hill-valley_1.csv',
    'robot-failures-lp4_1.csv',
    'kc1_1.csv',
    'segment_1.csv',
    'spectrometer_1.csv',
    'seismic-bumps_1.csv',
    'pc4_1.csv',
    'pc3_1.csv',
    'ada_agnostic_1.csv',
    'splice_2.csv',
    'bank-marketing_1.csv',
    'seeds_1.csv',
    'delta_ailerons_1.csv',
    'white-clover_1.csv',
    'boston_1.csv',
    'letter_1.csv',
    'prnn_viruses_1.csv',
    'oil_spill_1.csv',
    'credit-g_1.csv',
    'diabetes_1.csv',
    'boston_corrected_1.csv',
    'PieChart3_1.csv',
    'optdigits_1.csv',
    'PizzaCutter3_1.csv',
    'qsar-biodeg_1.csv',
    'abalone_1.csv',
    'cmc_2.csv',
    'iris_1.csv',
    'vinnie_1.csv',
    'pc1_1.csv',
    'balloon_1.csv',
    'tic-tac-toe_1.csv',
    'fri_c4_1000_100_1.csv',
    'robot-failures-lp3_1.csv',
    'autoUniv-au1-1000_1.csv',
    'lsvt_1.csv',
    'hill-valley_2.csv',
    'banana_1.csv',
    'vertebra-column_2.csv',
    'quake_1.csv',
    'rmftsa_sleepdata_1.csv',
    'kr-vs-kp_1.csv',
    'mfeat-zernike_1.csv',
    'wisconsin_1.csv',
    'CastMetal1_1.csv',
    'car_2.csv',
    'pendigits_1.csv',
    'PizzaCutter1_1.csv',
    'kc2_1.csv',
    'delta_elevators_1.csv',
    'mw1_1.csv',
    'analcatdata_asbestos_1.csv',
    'mu284_1.csv',
    'plasma_retinol_1.csv',
    'quake_2.csv',
    'socmob_1.csv',
    'PieChart1_1.csv',
    'housing_1.csv',
    'pasture_1.csv',
    'sensory_1.csv',
    'wine_2.csv',
    'chscase_geyser1_1.csv',
    'monks-problems-2_1.csv',
    'mfeat-pixel_1.csv',
    'analcatdata_dmft_1.csv',
    'autoPrice_1.csv',
    'SPECTF_1.csv',
    'breast-tissue_1.csv',
    'phoneme_1.csv',
    'vehicle_2.csv',
    'visualizing_soil_1.csv',
    'rabe_266_1.csv',
    'blood-transfusion-service-center_1.csv',
    'thoracic-surgery_1.csv',
    'ionosphere_1.csv',
    'pm10_1.csv',
    'sa-heart_1.csv',
    'analcatdata_authorship_2.csv',
    'jEdit_4.2_4.3_1.csv',
    'Australian_1.csv',
    'ecoli_1.csv',
    'ilpd_1.csv',
    'climate-model-simulation-crashes_1.csv',
    'pc1_req_1.csv',
    'sonar_1.csv',
    'mc2_1.csv',
    'auto_price_1.csv',
    'arsenic-female-bladder_1.csv',
    'kdd_synthetic_control_1.csv',
    'analcatdata_supreme_1.csv',
    'prnn_fglass_1.csv',
    'kin8nm_1.csv',
    'no2_1.csv',
    'vowel_1.csv',
    'pc2_1.csv',
    'fri_c4_1000_50_1.csv',
    'stock_1.csv',
    'tae_2.csv',
    'transplant_1.csv',
    'chscase_funds_1.csv',
    'SPECT_1.csv',
    'visualizing_galaxy_1.csv',
    'analcatdata_vineyard_1.csv',
    'newton_hema_1.csv',
    'puma8NH_1.csv',
    'fri_c4_500_100_1.csv',
    'wilt_1.csv',
    'analcatdata_germangss_1.csv',
    'dresses-sales_1.csv',
    'haberman_1.csv',
    'fri_c1_1000_50_1.csv',
    'fri_c2_1000_50_1.csv',
    'white-clover_2.csv',
    'ar4_1.csv',
    'chscase_vine2_1.csv',
    'balance-scale_2.csv',
    'CostaMadre1_1.csv',
    'diggle_table_a2_1.csv',
    'arsenic-male-bladder_1.csv',
    'sleuth_case2002_1.csv',
    'grub-damage_2.csv',
    'glass_1.csv',
    'rmftsa_ctoarrivals_1.csv',
    'jEdit_4.0_4.2_1.csv',
    'analcatdata_apnea1_1.csv',
    'prnn_cushings_1.csv',
    'pwLinear_1.csv',
    'analcatdata_apnea2_1.csv',
    'analcatdata_boxing2_1.csv',
    'visualizing_livestock_1.csv',
    'PieChart2_1.csv',
    'monks-problems-3_1.csv',
    'wholesale-customers_1.csv',
    'analcatdata_wildcat_1.csv',
    'fri_c3_1000_50_1.csv',
    'flags_1.csv',
    'analcatdata_cyyoung9302_1.csv',
    'fri_c3_1000_5_1.csv',
    'monks-problems-1_1.csv',
    'bodyfat_1.csv',
    'fri_c1_1000_25_1.csv',
    'fri_c3_1000_25_1.csv',
    'veteran_1.csv',
    'baskball_1.csv',
    'backache_1.csv',
    'kc3_1.csv',
    'kc1-binary_1.csv',
    'heart-statlog_1.csv',
    'fri_c0_1000_50_1.csv',
    'visualizing_ethanol_1.csv',
    'parkinsons_1.csv',
    'lowbwt_1.csv',
    'analcatdata_michiganacc_1.csv',
    'sleuth_ex1605_1.csv',
    'fruitfly_1.csv',
    'machine_cpu_1.csv',
    'tecator_1.csv',
    'triazines_1.csv',
    'pyrim_1.csv',
    'fri_c2_1000_10_1.csv',
    'lymph_2.csv',
    'fri_c3_500_50_1.csv',
    'fri_c0_1000_25_1.csv',
    'fri_c2_500_50_1.csv',
    'cloud_1.csv',
    'fri_c2_500_25_1.csv',
    'pollution_1_train.csv',
    'analcatdata_seropositive_1.csv',
    'pasture_2.csv',
    'analcatdata_lawsuit_1.csv',
    'dbworld-bodies_1.csv',
    'fri_c4_250_100_1.csv',
    'sleuth_ex2016_1.csv',
    'vineyard_1.csv',
    'analcatdata_apnea3_1.csv',
    'mfeat-morphological_1.csv',
    'analcatdata_boxing1_1.csv',
    'MegaWatt1_1.csv',
    'cm1_req_1.csv',
    'iris_2.csv',
    'fri_c2_1000_25_1.csv',
    'servo_1.csv',
    'fri_c3_1000_10_1.csv',
    'space_ga_1.csv',
    'nursery_2.csv',
    'fri_c4_1000_25_1.csv',
    'pollution_1.csv',
    'fri_c0_100_10_1.csv',
    'cpu_1.csv',
    'strikes_1.csv',
    'rabe_148_1.csv',
    'fri_c1_500_50_1.csv',
    'rmftsa_ladata_1.csv',
    'dbworld-subjects-stemmed_1.csv',
    'blogger_1.csv',
    'molecular-biology_promoters_1.csv',
    'kidney_1.csv',
    'fri_c1_500_25_1.csv',
    'fri_c2_250_50_1.csv',
    'diggle_table_a1_1.csv',
    'fri_c1_1000_10_1.csv',
    'sleuth_ex1221_1.csv',
    'analcatdata_vehicle_1.csv',
    'fl2000_1.csv',
    'kc1-top5_1.csv',
    'qualitative-bankruptcy_1.csv',
    'hutsof99_logis_1.csv',
    'sleuth_case1202_1.csv',
    'ar5_1.csv',
    'datatrieve_1.csv',
    'chscase_census4_1.csv',
    'analcatdata_cyyoung8092_1.csv',
    'acute-inflammations_1.csv',
    'fri_c3_250_25_1.csv',
    'chscase_census5_1.csv',
    'analcatdata_election2000_1.csv',
    'fri_c4_500_50_1.csv',
    'fri_c0_500_10_1.csv',
    'fri_c0_1000_10_1.csv',
    'hutsof99_child_witness_1.csv',
    'chscase_vine1_1.csv',
    'mbagrade_1.csv',
    'fri_c4_100_25_1.csv',
    'fri_c1_250_25_1.csv',
    'fri_c2_250_25_1.csv',
    'acute-inflammations_2.csv',
    'fri_c3_500_5_1.csv',
    'sleuth_case1102_1.csv',
    'fri_c2_100_25_1.csv',
    'analcatdata_gviolence_1.csv',
    'banknote-authentication_1.csv',
    'humandevel_1.csv',
    'fri_c0_500_50_1.csv',
    'chscase_health_1.csv',
    'pollution_1_test.csv',
    'fri_c0_250_50_1.csv',
    'fertility_1.csv',
    'chscase_census2_1.csv',
    'pollen_1.csv',
    'ar1_1.csv',
    'fri_c1_250_50_1.csv',
    'dbworld-subjects_1.csv',
    'arsenic-female-lung_1.csv',
    'fri_c0_100_25_1.csv',
    'schlvote_1.csv',
    'ar3_1.csv',
    'disclosure_x_bias_1.csv',
    'vertebra-column_1.csv',
    'fri_c4_500_25_1.csv',
    'molecular-biology_promoters_2.csv',
    'hayes-roth_1.csv',
    'fri_c3_100_50_1.csv',
    'disclosure_x_noise_1.csv',
    'wind_correlations_1.csv',
    'fri_c3_100_10_1.csv',
    'visualizing_environmental_1.csv',
    'fri_c2_100_5_1.csv',
    'fri_c4_250_10_1.csv',
    'fri_c4_100_100_1.csv',
    'fri_c0_250_10_1.csv',
    'wdbc_1.csv',
    'fri_c1_100_50_1.csv',
    'fri_c0_100_5_1.csv',
    'confidence_1.csv',
    'analcatdata_bankruptcy_1.csv',
    'fri_c3_100_5_1.csv',
    'fri_c0_250_25_1.csv',
    'elusage_1.csv',
    'fri_c4_100_50_1.csv',
    'sleuth_case1201_1.csv',
    'fri_c1_100_25_1.csv',
    'chatfield_4_1.csv',
    'analcatdata_chlamydia_1.csv',
    'fri_c2_500_5_1.csv',
    'chscase_census6_1.csv',
    'fri_c4_250_25_1.csv',
    'aids_1.csv',
    'bolts_1.csv',
    'fri_c0_500_25_1.csv',
    'fri_c4_1000_10_1.csv',
    'fri_c2_100_50_1.csv',
    'rabe_97_1.csv',
    'fri_c3_250_50_1.csv',
    'analcatdata_olympic2000_1.csv',
    'planning-relax_1.csv',
    'collins_1.csv',
    'rabe_265_1.csv',
    'sleuth_ex2015_1.csv',
    'fri_c1_250_10_1.csv',
    'fri_c0_1000_5_1.csv',
    'lupus_1.csv',
    'visualizing_hamster_1.csv',
    'sleuth_ex1714_1.csv',
    'chscase_adopt_1.csv',
    'fri_c1_500_5_1.csv',
    'fri_c2_1000_5_1.csv',
    'fri_c3_500_25_1.csv',
    'fri_c4_250_50_1.csv',
    'rabe_131_1.csv',
    'fri_c3_250_10_1.csv',
    'zoo_1.csv',
    'ar6_1.csv',
    'witmer_census_1980_1.csv',
    'fri_c0_100_50_1.csv',
    'analcatdata_challenger_1.csv',
    'fri_c4_500_10_1.csv',
    'fri_c1_100_5_1.csv',
    'fri_c2_500_10_1.csv',
    'fri_c3_100_25_1.csv',
    'fri_c2_250_10_1.csv',
    'fri_c3_500_10_1.csv',
    'rabe_166_1.csv',
    'fri_c3_250_5_1.csv',
    'fri_c0_500_5_1.csv',
    'analcatdata_creditscore_1.csv',
    'chscase_census3_1.csv',
    'fri_c1_1000_5_1.csv',
    'fri_c2_100_10_1.csv',
    'fri_c1_500_10_1.csv',
    'prnn_synth_1.csv',
    'fri_c0_250_5_1.csv',
    'badges2_1.csv',
    'fri_c2_250_5_1.csv',
    'visualizing_slope_1.csv',
    'disclosure_x_tampered_1.csv',
    'fri_c1_100_10_1.csv',
    'analcatdata_neavote_1.csv',
    'disclosure_z_1.csv',
    'diabetes_numeric_1.csv',
    'analcatdata_challenger_2.csv',
    'fri_c1_250_5_1.csv',
    'fri_c4_100_10_1.csv',
    'rabe_176_1.csv',
    'arsenic-male-lung_1.csv',
    'sleuth_ex2016_2.csv',
    'sleuth_ex2015_2.csv',
    'analcatdata_japansolvent_1.csv'
    'Australian_4.csv',
    'Bioresponse_1.csv',
    'GesturePhaseSegmentationProcessed_1.csv',
    'JapaneseVowels_1.csv',
    'KDDCup09_churn_1.csv',
    'KDDCup09_upselling_1.csv',
    'LED-display-domain-7digit_1.csv',
    'MiceProtein_1.csv',
    'SpeedDating_1.csv',
    'adult_2.csv',
    'artificial-characters_1.csv',
    'breast-w_1.csv',
    'cjs_3.csv',
    'cnae-9_1.csv',
    'connect-4_2.csv',
    'credit-approval_1.csv',
    'cylinder-bands_2.csv',
    'dresses-sales_2.csv',
    'eucalyptus_1.csv',
    'first-order-theorem-proving_1.csv',
    'gas-drift_1.csv',
    'gina_agnostic_1.csv',
    'har_1.csv',
    'higgs_2.csv',
    'irish_1.csv',
    'isolet_1.csv',
    'jm1_1.csv',
    'micro-mass_2.csv',
    'mnist_784_1.csv',
    'mushroom_1.csv',
    'nomao_1.csv',
    'one-hundred-plants-margin_1.csv',
    'one-hundred-plants-shape_1.csv',
    'one-hundred-plants-texture_1.csv',
    'profb_1.csv',
    'satimage_1.csv',
    'semeion_1.csv',
    'sick_1.csv',
    'soybean_1.csv',
    'sylva_agnostic_1.csv',
    'synthetic_control_1.csv',
    'tamilnadu-electricity_1.csv',
    'texture_1.csv',
    'vowel_2.csv'
]

# Only the OPENML 100 datasets
OPENML100 = [
    'connect-4_2.csv',
    'Australian_4.csv',
    'kr-vs-kp_1.csv',
    'letter_1.csv',
    'balance-scale_1.csv',
    'mfeat-factors_1.csv',
    'mfeat-fourier_1.csv',
    'breast-w_1.csv',
    'mfeat-karhunen_1.csv',
    'mfeat-morphological_1.csv',
    'mfeat-pixel_1.csv',
    'car_1.csv',
    'mfeat-zernike_1.csv',
    'cmc_1.csv',
    'mushroom_1.csv',
    'optdigits_1.csv',
    'credit-approval_1.csv',
    'credit-g_1.csv',
    'pendigits_1.csv',
    'segment_1.csv',
    'diabetes_1.csv',
    'sick_1.csv',
    'soybean_1.csv',
    'spambase_1.csv',
    'splice_1.csv',
    'tic-tac-toe_1.csv',
    'vehicle_1.csv',
    'waveform-5000_1.csv',
    'electricity_1.csv',
    'satimage_1.csv',
    'eucalyptus_1.csv',
    'isolet_1.csv',
    'vowel_2.csv',
    'scene_1.csv',
    'monks-problems-1_1.csv',
    'monks-problems-2_1.csv',
    'monks-problems-3_1.csv',
    'JapaneseVowels_1.csv',
    'synthetic_control_1.csv',
    'irish_1.csv',
    'analcatdata_authorship_1.csv',
    'analcatdata_dmft_1.csv',
    'profb_1.csv',
    'collins_1.csv',
    'mnist_784_1.csv',
    'sylva_agnostic_1.csv',
    'gina_agnostic_1.csv',
    'ada_agnostic_1.csv',
    'mozilla4_1.csv',
    'pc4_1.csv',
    'pc3_1.csv',
    'jm1_1.csv',
    'kc2_1.csv',
    'kc1_1.csv',
    'pc1_1.csv',
    'KDDCup09_churn_1.csv',
    'KDDCup09_upselling_1.csv',
    'MagicTelescope_1.csv',
    # 'Internet-Advertisements_1.csv',  Not Available https://www.openml.org/d/1176
    'artificial-characters_1.csv',
    'bank-marketing_1.csv',
    'banknote-authentication_1.csv',
    'blood-transfusion-service-center_1.csv',
    'cardiotocography_1.csv',
    'climate-model-simulation-crashes_1.csv',
    'cnae-9_1.csv',
    'eeg-eye-state_1.csv',
    'first-order-theorem-proving_1.csv',
    'gas-drift_1.csv',
    'har_1.csv',
    'hill-valley_1.csv',
    'ilpd_1.csv',
    'madelon_1.csv',
    'nomao_1.csv',
    'ozone-level-8hr_1.csv',
    'phoneme_1.csv',
    'one-hundred-plants-margin_1.csv',
    'one-hundred-plants-shape_1.csv',
    'one-hundred-plants-texture_1.csv',
    'qsar-biodeg_1.csv',
    'wall-robot-navigation_1.csv',
    'semeion_1.csv',
    'steel-plates-fault_1.csv',
    'tamilnadu-electricity_1.csv',
    'wdbc_1.csv',
    'micro-mass_2.csv',
    'wilt_1.csv',
    'Bioresponse_1.csv',
    'Amazon_employee_access_1.csv',
    'PhishingWebsites_1.csv',
    'GesturePhaseSegmentationProcessed_1.csv',
    'MiceProtein_1.csv',
    'chscase_census2_1.csv',
    'cylinder-bands_2.csv',
    'cjs_3.csv',
    'dresses-sales_2.csv',
    'higgs_2.csv',
    'LED-display-domain-7digit_1.csv',
    'texture_1.csv',
    'SpeedDating_1.csv',
    'adult_2.csv',
]


AVAILABLE_CHALLENGES = {
    'all': ALL_DATASETS_BY_TIME.copy(),
    'openml100': OPENML100.copy(),
}


def get_dataset_names(collection):
    try:
        return AVAILABLE_CHALLENGES[collection.lower()]
    except KeyError:
        collections = ', '.join(AVAILABLE_CHALLENGES.keys())
        raise ValueError('Currently the available collections are: {}'.format(collections))
