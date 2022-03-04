# import libraries
from osgeo import gdal, osr
import os
import fiona
import rasterio
from rasterio.mask import mask
from rasterio.plot import show

# load the data
def load_data(opt, path=None):
    if opt == 1:
        img = gdal.Open(path)
        shapefile = fiona.open('/path/to/shapefile.shp')
        return img, shapefile
    else:
        raster = rasterio.open("/path/to/reprojected/raster.tif")
        return raster 

# reproject the data
def reproject(img):
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    new_projection = srs.ExportToWkt()
    gdal.Warp("/path/to/reprojected/raster.tif", img, dstSRS=new_projection)

# clip the raster image
def clip_raster(shapefile):
    raster = load_data(2)
    shapes = [feature["geometry"] for feature in shapefile]
    
    crop_image, crop_transform = mask(raster, shapes, crop=True)
    crop_meta = raster.meta
    crop_meta.update({"driver": "GTiff",
                 "height": crop_image.shape[1],
                 "width": crop_image.shape[2],
                 "transform": crop_transform})

    with rasterio.open("/path/to/clipped/raster.tif", "w", **crop_meta) as dest:
        dest.write(crop_image)

# driver code
if __name__ == '__main__':

    path = "/path/to/sentinel-1/imagery.tif"

    img, shapefile = load_data(1, path)

    reproject(img) 

    clip_raster(shapefile)
