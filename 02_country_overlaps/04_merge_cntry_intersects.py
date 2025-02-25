import os
import glob
import rsgislib.vectorutils

gmw_cntry_diffs = glob.glob("/Users/pfb/Temp/gmw_v4_un_eez_chks/countries_intersections_20250225/*.gpkg")


rsgislib.vectorutils.merge_vector_files(vec_files = gmw_cntry_diffs, out_vec_file = "eez_un_diss_20250225_cntry_intersects.gpkg", out_vec_lyr = "eez_un_diss_20250225_cntry_intersects", out_format = 'GPKG', out_epsg = None, remove_cols = None)

