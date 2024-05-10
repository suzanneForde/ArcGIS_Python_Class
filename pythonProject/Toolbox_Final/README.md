# ArcGIS Toolbox (Final Assignment)

This Python Toolbox consists of three geoprocessing tools designed for common operations on spatial data using ArcPy. Each tool serves a specific purpose and can be used individually or as part of a larger workflow.

## Tools

### 1. Field Lister Tool

The Field Lister Tool lists the fields of a shapefile, providing users with insights into the attribute structure of their spatial data.

#### Usage

- **Input Shapefile**: Select the shapefile for which you want to list the fields.

### 2. Buffer Tool

The Buffer Tool creates a buffer around features in a feature class based on a specified buffer distance. Buffers are commonly used in spatial analysis to analyze proximity or create visual representations of spatial relationships.

#### Usage

- **Input Feature**: Select the feature class you want to buffer.
- **Output Feature**: Specify the output feature class where the buffered features will be saved.
- **Buffer Distance**: Define the distance for the buffer zone around features.

### 3. Polygon Area Tool

The Polygon Area Tool calculates the area of a single polygon feature within a feature class. This tool provides valuable information for analyzing spatial data, such as land area estimation or spatial pattern analysis.

#### Usage

- **Input Polygon**: Choose the polygon feature for which you want to calculate the area.
- **Output Area**: The calculated area of the input polygon.


Feel free to utilize and modify these tools to suit your specific GIS needs.


## Example Data

To test the functionality of each tool, you can use the example datasets from the provided Data_Folder. I recommend adding each shapefile to your map contents pane.

- Field Lister Tool: After opening this tool, you can use any of the files provided. Once the tool is run, the "messages" tab will list all fields in file.

- Buffer Tool: Select the "State_Comprehensive_Outdoor_Recreation_Plan_Inventory_of_Facilities". Provide a name for your output feature. Input buffer distance and unit of measurement. Run the tool. If you navigate to the provided geodatabase, and open the shapefile with the name "Recreation_buffer" in ArcGIS, you will see the shapefile I created with the tool using an input of .5 miles to create the buffer around outdoor recreation in RI.

- Polygon Area Tool: Use the provided "Municipalities_(1997)" shapefile and select a preferred unit of measurement.

## Installation

1. Download the `Geoprocessing_Toolbox.pyt` file.
2. Open ArcGIS Pro or ArcMap.
3. In the Catalog pane, right-click on Toolboxes and select "Add Toolbox..."
4. Browse to the location of `Geoprocessing_Toolbox.pyt` and add it to your project.


### Data provided by RIGIS.org
