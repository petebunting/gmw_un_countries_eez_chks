import tqdm
import os
import glob
import rsgislib.vectorutils
import rsgislib.vectorgeoms

gmw_vec_files = glob.glob("gmw_v4023_tiles/S*.gpkg")

out_dir = "gmw_v4023_tiles_diff"

un_cntry_vec_file = "eez_un_diss_20250213.gpkg"
un_cntry_vec_lyr = "eez_un_diss_20250213"

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
    
