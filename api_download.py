# import libraries
import sentinelsat
import geopandas
from sentinelsat import geojson_to_wkt, read_geojson, SentinelAPI
from collections import OrderedDict


class Download:
    
    def __init__(self):
        self.myshpfile = None
        self.footprint = None
        pass
    
    # Convert shapefile to geojson
    def convert(self):

        self.myshpfile = geopandas.read_file('./shapefile/myshapefile.shp')
        self.myshpfile.to_file('./geojson/myJson.geojson', driver='GeoJSON')
        self.footprint = geojson_to_wkt(read_geojson('./geojson/myJson.geojson'))

    # Query products
    def query(self):
        self.api = SentinelAPI('username', 'password', 'https://apihub.copernicus.eu/apihub')
        
        Date1 = input("Enter start date (Format:YYYYMMDD)")
        Date2 = input("Enter end date (Format:YYYYMMDD)")
        
        # ordered dictionary to store the data specification from the query result.
        # print this to find the product specification and accordingly you can sort the products of your choice.
        self.products = self.api.query(self.footprint,
                             date = (Date1,Date2),
                             platformname = 'Sentinel-1'
                             )
        
    # Fetch old products and sort them by month
    def fetch(self):
        self.productsID = list(self.products)
        self.GRD_products = dict()
        
        for i in range(len(self.productsID)):
            x = self.products[self.productsID[i]]['beginposition']
            month = int(x.strftime("%m"))
            if self.products[self.productsID[i]]["producttype"] == "GRDH" and self.products[self.productsID[i]]["sensoroperationalmode"] == "IW":
                self.GRD_products.setdefault(month, list()).append(self.productsID[i])
    
    # Download the data, one image per month
    def download_one(self):
        
        for key, value in self.GRD_products.items():
            for i in range(len(value)):
                    try:
                        self.api.download(self.GRD_products[key][i],'data')
                        break
                    except:
                        pass
        
    # Download all data
    def download_all(self):
        
        for key, value in self.GRD_products.items():
            for i in range(len(value)):
                    try:
                        self.api.download(self.GRD_products[key][i],'data')
                    except:
                        pass
                
                
    # Download new data
    def download(self):
        if not self.footprint:
            self.convert()
        self.query()
        
    
    
if __name__=='__main__':
    API = Download()
    while True:
        opt = int(input("Select from following.\n1. Download one image per month.\n2. Download all images\n3. Exit\nEnter: "))
        if opt == 1:
            API.download()
            API.fetch()
            API.download_one()
            print("\n")
        elif opt == 2:
            API.download()
            API.fetch()
            API.download_all()
            print("\n")
        else:
            break