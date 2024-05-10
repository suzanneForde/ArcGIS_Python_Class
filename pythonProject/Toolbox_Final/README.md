# ArcGIS Toolbox (Final Assignment)

This Python Toolbox contains three geoprocessing tools designed to perform common operations on spatial data using ArcPy. Each tool serves a specific purpose and can be used individually or as part of a larger workflow.

## Tools

### 1. Shapefile Renamer Tool

The Shapefile Renamer Tool allows you to rename a shapefile to a new name of your choice. This tool is useful for organizing and managing spatial datasets within a GIS environment.

#### Usage

- **Input Shapefile**: Select the shapefile you want to rename.
- **New Name**: Specify the new name for the shapefile.

### 2. Area Calculator Tool

The Area Calculator Tool calculates the total area of features in a feature class and allows you to specify the output unit (square meters, acres, or square feet). This tool is handy for estimating land area or analyzing spatial data.

#### Usage

- **Input Feature**: Choose the feature class for which you want to calculate the area.
- **Output Unit**: Select the desired unit for the calculated area (square meters, acres, or square feet).

### 3. Buffer Tool

The Buffer Tool creates a buffer around features in a feature class based on a specified buffer distance. Buffers are commonly used in spatial analysis to analyze proximity or create visual representations of spatial relationships.

#### Usage

- **Input Feature**: Select the feature class you want to buffer.
- **Output Feature**: Specify the output feature class where the buffered features will be saved.
- **Buffer Distance**: Define the distance for the buffer zone around features.

## Example Data

To test the functionality of each tool, you can use the example datasets from the provided Data_Folder. I recommend adding each shapefile to your map contents pane.

- Shapefile Renamer Tool: After opening this tool, you will see a drop-down option. Use the "State_Comprehensive_Outdoor_Recreation_Plan_Inventory_of_Facilities.shp" and input "RI_Recreation" in the "New Name" parameter. Run the tool.

- Area Calculator Tool: Select "State_Boundary_(1997).shp" shapefile by using drop-down option to calculate the area of the state of Rhode Island. Select your preferred unit. Run the tool.

- Buffer Tool: Select the "RI_DOT_Bike_Paths.shp" shapefile using the drop-down function. Provide a name for your output feature. Input buffer distance and unit of measurement. Run the tool.

## Installation

1. Download the `Geoprocessing_Toolbox.pyt` file.
2. Open ArcGIS Pro or ArcMap.
3. In the Catalog pane, right-click on Toolboxes and select "Add Toolbox..."
4. Browse to the location of `Geoprocessing_Toolbox.pyt` and add it to your project.


### Data provided by RIGIS.org
