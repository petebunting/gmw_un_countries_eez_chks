import rsgislib.vectorutils

rsgislib.vectorutils.split_vec_lyr(
    vec_file = "eez_un_diss_20250213.gpkg",
    vec_lyr = "eez_un_diss_20250213",
    n_feats = 1,
    out_format = "GPKG",
    out_dir = "country_units",
    out_vec_base = "eez_un_diss_20250213_",
    out_vec_ext = "gpkg",
)