import os
import glob
import rsgislib.vectorutils

gmw_cntry_diffs = glob.glob("gmw_v4023_tiles_diff/*.gpkg")


rsgislib.vectorutils.merge_vector_files(vec_files = gmw_cntry_diffs, out_vec_file = "eez_un_diss_20250213_gmw_v4023_diff.geojson", out_vec_lyr = "eez_un_diss_20250213_gmw_v4023_diff", out_format = 'GeoJSON', out_epsg = None, remove_cols = None)

