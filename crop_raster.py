from osgeo import gdal, osr
import os
import fiona
import rasterio
from rasterio.mask import mask
from rasterio.plot import show

def load_data(opt, path=None):
    if opt == 1:
        img = gdal.Open(path[0]+"/"+os.listdir(path[0])[0])
        shapefile = fiona.open('./shapefile/marni_plot1.shp')
        return img, shapefile
    else:
        raster = rasterio.open("./output_data/reproject_input.tif")
        return raster 

def reproject(img):
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    new_projection = srs.ExportToWkt()
    gdal.Warp("./output_data/reproject_input.tif", img, dstSRS=new_projection)

def clip_raster(shapefile):
    raster = load_data(2)
    shapes = [feature["geometry"] for feature in shapefile]
    
    out_image, out_transform = mask(raster, shapes, crop=True)
    out_meta = raster.meta
    out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

    with rasterio.open("./output_data/clip_raster.tif", "w", **out_meta) as dest:
        dest.write(out_image)
    
#     display_raster(dest)

# def display_raster(output_img):
#     show(output_img)
    

if __name__ == '__main__':

    data_dir = sorted(os.listdir("data"))
    path = list(map(lambda x: "data/"+x+"/measurement", data_dir))

    img, shapefile = load_data(1, path)

    reproject(img) 

    clip_raster(shapefile)
