import rsgislib.tools.utils
import os
import rsgislib.vectorgeoms
import tqdm


in_vec_dir = "/Users/pfb/Temp/gmw_v4_un_eez_chks/country_units_20250225"
out_vec_dir = "/Users/pfb/Temp/gmw_v4_un_eez_chks/countries_intersections_20250225"


intersect_lut = rsgislib.tools.utils.read_json_to_dict("country_rgn_intersects.json")
intersect_lut_chkd = dict()

for base_cntry in tqdm.tqdm(intersect_lut, position=0, leave=True):
    intersect_lut_chkd[base_cntry] = list()

    base_vec_file = os.path.join(in_vec_dir, f"{base_cntry}.gpkg")
    base_vec_lyr = rsgislib.vectorutils.get_vec_lyrs_lst(base_vec_file)[0]

    for cmp_cntry in tqdm.tqdm(intersect_lut[base_cntry], position=1, leave=False):

        cmp_vec_file = os.path.join(in_vec_dir, f"{cmp_cntry}.gpkg")
        cmp_vec_lyr = rsgislib.vectorutils.get_vec_lyrs_lst(cmp_vec_file)[0]

        skip = False
        if cmp_cntry in intersect_lut_chkd:
            if base_cntry in intersect_lut_chkd[cmp_cntry]:
                skip = True

        if not skip:

            out_vec_lyr = f"{base_cntry}_{cmp_cntry}"
            out_vec_file = os.path.join(out_vec_dir, f"{out_vec_lyr}.gpkg")
            if not os.path.exists(out_vec_file):
                print(f"Create {out_vec_file}")
                try:
                    rsgislib.vectorgeoms.vec_lyr_intersection_gp(
                        base_vec_file,
                        base_vec_lyr,
                        cmp_vec_file,
                        cmp_vec_lyr,
                        out_vec_file,
                        out_vec_lyr,
                        out_format="GPKG",
                        del_exist_vec=False,
                    )
                    intersect_lut_chkd[base_cntry].append(cmp_cntry)
                except Exception as e:
                    print(e)
                    continue