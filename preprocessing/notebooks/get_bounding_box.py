import geopandas as gpd
from shapely.geometry import box

def get_bounding_box(gpd_object, buffer_size=0, target_crs=None):
    """
    Returns the bounding box of a geopandas object

    Parameters
    ----------
    gpd_object : geopandas object
        The geopandas object to get the bounding box of
    buffer_size : int
        The buffer size to add to the bounding box

    Returns
    -------
    bounding_box : geopandas series
        The bounding box of the geopandas object
    """
    minx, miny, maxx, maxy = gpd_object.bounds.values.ravel().tolist()
    minx, miny, maxx, maxy = minx - buffer_size, miny - buffer_size, maxx + buffer_size, maxy + buffer_size
    bounding_poly = box(minx, miny, maxx, maxy)
    bounding_series = gpd.GeoSeries([bounding_poly], crs=gpd_object.crs)

    if target_crs is not None:
        bounding_series = bounding_series.to_crs(target_crs)

    return bounding_series
