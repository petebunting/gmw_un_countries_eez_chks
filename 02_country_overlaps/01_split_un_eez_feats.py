import rsgislib.vectorutils

rsgislib.vectorutils.split_vec_lyr(
    vec_file = "../01_gmw_diff/mangrove_statistics_areas_20250225.gpkg",
    vec_lyr = "mangrove_statistics_areas_20250225",
    n_feats = 1,
    out_format = "GPKG",
    out_dir = "/Users/pfb/Temp/gmw_v4_un_eez_chks/country_units_20250225",
    out_vec_base = "eez_un_diss_20250225_",
    out_vec_ext = "gpkg",
)