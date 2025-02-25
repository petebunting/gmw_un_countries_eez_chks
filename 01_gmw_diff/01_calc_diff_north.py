import tqdm
import os
import glob
import rsgislib.vectorutils
import rsgislib.vectorgeoms

gmw_vec_files = glob.glob("/Users/pfb/Temp/gmw_v4_un_eez_chks/gmw_v4023_tiles/N*.gpkg")

out_dir = "/Users/pfb/Temp/gmw_v4_un_eez_chks/gmw_v4023_tiles_diff_20250225"

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

un_cntry_vec_file = "mangrove_statistics_areas_20250225.gpkg"
un_cntry_vec_lyr = "mangrove_statistics_areas_20250225"

for gmw_vec_file in tqdm.tqdm(gmw_vec_files):
    gmw_vec_lyr = rsgislib.vectorutils.get_vec_lyrs_lst(gmw_vec_file)[0]

    out_vec_file = os.path.join(out_dir, f"{gmw_vec_lyr}_diff.gpkg")
    out_vec_lyr = f"{gmw_vec_lyr}_diff"
    
    rsgislib.vectorgeoms.vec_lyr_difference_gp(
        vec_file=gmw_vec_file,
        vec_lyr=gmw_vec_lyr,
        vec_over_file=un_cntry_vec_file,
        vec_over_lyr=un_cntry_vec_lyr,
        out_vec_file=out_vec_file,
        out_vec_lyr=out_vec_lyr,
        out_format="GPKG",
        del_exist_vec=False,
    )
    
