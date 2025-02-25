import os
import glob
import tqdm
import rsgislib.vectorgeoms
from osgeo import gdal
import rsgislib.tools.utils


def vec_intersects_vec(
    vec_base_file: str, vec_base_lyr: str, vec_comp_file: str, vec_comp_lyr: str
) -> bool:
    """
    Function to test whether the comparison vector layer intersects with the
    base vector layer.

    Note. This function iterates through the geometries of both files performing
    a comparison and therefore can be very slow to execute for large vector files.

    :param vec_base_file: vector layer file used as the base layer
    :param vec_base_lyr: vector layer used as the base layer
    :param vec_comp_file: vector layer file used as the comparison layer
    :param vec_comp_lyr: vector layer used as the comparison layer
    :return: boolean

    """
    import tqdm

    dsVecBaseObj = gdal.OpenEx(vec_base_file, gdal.OF_READONLY)
    if dsVecBaseObj is None:
        raise rsgislib.RSGISPyException("Could not open '{}'".format(vec_base_file))

    lyrVecBaseObj = dsVecBaseObj.GetLayerByName(vec_base_lyr)
    if lyrVecBaseObj is None:
        raise rsgislib.RSGISPyException(
            "Could not find layer '{}'".format(vec_base_lyr)
        )

    dsVecCompObj = gdal.OpenEx(vec_comp_file, gdal.OF_READONLY)
    if dsVecCompObj is None:
        raise rsgislib.RSGISPyException("Could not open '{}'".format(vec_comp_file))

    lyrVecCompObj = dsVecCompObj.GetLayerByName(vec_comp_lyr)
    if lyrVecCompObj is None:
        raise rsgislib.RSGISPyException(
            "Could not find layer '{}'".format(vec_comp_lyr)
        )

    n_feats = lyrVecBaseObj.GetFeatureCount(True)
    #pbar = tqdm.tqdm(total=n_feats)
    does_intersect = False
    lyrVecBaseObj.ResetReading()
    base_feat = lyrVecBaseObj.GetNextFeature()
    while base_feat is not None:
        base_geom = base_feat.GetGeometryRef()
        if base_geom is not None:
            lyrVecCompObj.ResetReading()
            comp_feat = lyrVecCompObj.GetNextFeature()
            while comp_feat is not None:
                comp_geom = comp_feat.GetGeometryRef()
                if comp_geom is not None:
                    if base_geom.Intersects(comp_geom):
                        does_intersect = True
                        break
                comp_feat = lyrVecCompObj.GetNextFeature()
        if does_intersect:
            break
        #pbar.update(1)
        base_feat = lyrVecBaseObj.GetNextFeature()

    dsVecBaseObj = None
    dsVecCompObj = None

    return does_intersect


cntry_vec_files = glob.glob("/Users/pfb/Temp/gmw_v4_un_eez_chks/country_units_20250225/*.gpkg")

intersect_lut = dict()

for cntry_vec_file in tqdm.tqdm(cntry_vec_files, position=0, leave=False):
    cntry_vec_lyr = rsgislib.vectorutils.get_vec_lyrs_lst(cntry_vec_file)[0]
    intersect_lut[cntry_vec_lyr] = list()
    
    for inner_cntry_vec_file in tqdm.tqdm(cntry_vec_files, position=1, leave=False):
        inner_cntry_vec_lyr = rsgislib.vectorutils.get_vec_lyrs_lst(inner_cntry_vec_file)[0]
        
        if inner_cntry_vec_file == cntry_vec_file:
            continue
        
        intersect = vec_intersects_vec(cntry_vec_file, cntry_vec_lyr, inner_cntry_vec_file, inner_cntry_vec_lyr)
        
        if intersect:
            intersect_lut[cntry_vec_lyr].append(inner_cntry_vec_lyr)
            
rsgislib.tools.utils.write_dict_to_json(intersect_lut, out_file = "country_rgn_intersects.json")


