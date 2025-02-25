import os
import glob
import rsgislib.vectorutils

gmw_cntry_diffs = glob.glob("countries_intersections/*.gpkg")


rsgislib.vectorutils.merge_vector_files(vec_files = gmw_cntry_diffs, out_vec_file = "eez_un_diss_20250213_cntry_intersects.gpkg", out_vec_lyr = "eez_un_diss_20250213_cntry_intersects", out_format = 'GPKG', out_epsg = None, remove_cols = None)

