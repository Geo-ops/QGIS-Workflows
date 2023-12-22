# To run this script first amend the file paths in lines 20, 23 and 26.

# Open QGIS
# Open the python console 

# Input the following into the Qgis python console: 
#       import sys
#       sys.path.append(r'file\path\to\this\python\script\location')
#       import kmltocsv 

# Note - Do not add the file type .py to the last step


import os
import csv
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *

# Set the path to the KML file
kml_file = r'C:\your\file\path.kml'

# Set the path to the output shapefile
shapefile = r'C:\your\file\path.shp'

# Set the path to the output CSV file
csv_file = r'C:\your\file\path.csv'

# Initialize QGIS
app = QgsApplication([], False)
QgsApplication.setPrefixPath('/usr', True)
QgsApplication.initQgis()

# Load the KML file
layer = QgsVectorLayer(kml_file, 'layer_name', 'ogr')

# Save the layer as a shapefile
# Required so the attribute table can be edited
options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = 'ESRI Shapefile'
options.fileEncoding = 'utf-8'
QgsVectorFileWriter.writeAsVectorFormat(layer, shapefile, options)

# Load the shapefile
layer = QgsVectorLayer(shapefile, 'layer_name', 'ogr')

# Create a CSV file for writing
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Latitude', 'Longitude'])

    # Loop through each feature and extract the name, latitude, and longitude
    for feature in layer.getFeatures():
        name = feature['Name']
        latitude = feature.geometry().asPoint().y()
        longitude = feature.geometry().asPoint().x()

        # Write the name, latitude, and longitude to the CSV file
        writer.writerow([name, latitude, longitude])

# Exit QGIS
QgsApplication.exitQgis()