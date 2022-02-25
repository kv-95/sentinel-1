# Sentinel-1 Data Download Using API

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Logo](Sentinel-1.jpg)

Satellite images are widely being used in the field of GIS and Remote Sensing these days. ESA and USGS are some of the organizations who provide free access to high resolution satellite data. 

There are 2 ways by which we can access satellite data. One is through their website using GUI, the other method is through API calls. First method is easy and simple to use but isn't suited if we are downloading the data on a regular basis. 

The python code provided in this repo is for downloading sentinel-1 dataset from [Copernicus Open Access Hub](https://scihub.copernicus.eu/dhus/#/home). sentinel-1 uses microwaves backscattered from the ground and is not influenced by cloud cover or vegetation. There are several advantages for using API for downloading the satellite data.

* Best suited for downloading large amounts of data on regular basis
* Easy customization of accessing the datasets
* Easy to access the data that is offline (Access data from Long Time Archives(LSA))
<hr>

_**Product Specification**_

* Product Type &#8594; High resolution Ground Range Detected (GRDH) 
* Sensor operation mode &#8594; Interferometric Wide swath (IW)

_**Functionalities in code:**_

* Download one image per month in a specified time period
* Download all the images available in the specified time period.

<hr>

_**Happy Coding!!**_	:computer: