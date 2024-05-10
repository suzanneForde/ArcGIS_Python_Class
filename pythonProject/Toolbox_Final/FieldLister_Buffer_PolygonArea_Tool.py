
###
# Toolbox Final
###

# For this final project toolbox I decided to use three tools.
# The first tool is field lister tool which lists all fields within the input shapefile.
# The second is the buffer which runs an analysis on your input shapefile.
# The third tool calculates the area of the input polygon feature.


import arcpy


# Define FieldListerTool class
class FieldListerTool(object):
    def __init__(self):
        self.label = "Field Lister Tool"  # Tool label
        self.description = "List the fields of a shapefile."  # Tool description
        self.canRunInBackground = False  # Set whether the tool can run in the background

    def getParameterInfo(self):
        params = [
            arcpy.Parameter(
                displayName="Input Shapefile",
                name="input_shapefile",
                datatype="DEShapefile",
                parameterType="Required",
                direction="Input"
            )
        ]
        return params

    def isLicensed(self):
        return True  # Set whether the tool is licensed to execute

    def execute(self, parameters, messages):
        input_shapefile = parameters[0].valueAsText  # Get input shapefile

        # List the fields of the input shapefile
        field_names = [field.name for field in arcpy.ListFields(input_shapefile)]
        arcpy.AddMessage("Fields of the shapefile:")
        for field_name in field_names:
            arcpy.AddMessage(field_name)


# Define BufferTool class
class BufferTool(object):
    def __init__(self):
        self.label = "Buffer Tool"  # Tool label
        self.description = "Buffer a feature."  # Tool description
        self.canRunInBackground = False  # Set whether the tool can run in the background

    def getParameterInfo(self):
        # Define input parameters for tool
        params = [
            arcpy.Parameter(
                displayName="Input Feature",
                name="input_feature",
                datatype="Feature Layer",  # Change datatype to Feature Layer
                parameterType="Required",
                direction="Input"
            ),
            arcpy.Parameter(
                displayName="Output Feature",
                name="output_feature",
                datatype="Feature Layer",  # Change datatype to Feature Layer
                parameterType="Required",
                direction="Output"
            ),
            arcpy.Parameter(
                displayName="Buffer Distance",
                name="buffer_distance",
                datatype="GPLinearUnit",
                parameterType="Required",
                direction="Input"
            )
        ]
        return params

    def isLicensed(self):
        return True  # Set whether the tool is licensed to execute

    def execute(self, parameters, messages):
        input_feature = parameters[0].valueAsText  # Get input feature
        output_feature = parameters[1].valueAsText  # Get output feature
        buffer_distance = parameters[2].valueAsText  # Get buffer distance
        arcpy.Buffer_analysis(input_feature, output_feature, buffer_distance)


class PolygonAreaTool(object):
    def __init__(self):
        self.label = "Polygon Area Tool"
        self.description = "Calculate the area of a single polygon feature."
        self.canRunInBackground = False

    def getParameterInfo(self):
        choices = ["Square Kilometers", "Square Meters", "Square Miles", "Square Feet"]
        param = arcpy.Parameter(
            displayName="Unit of Measurement",
            name="unit",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param.filter.type = "ValueList"
        param.filter.list = choices

        params = [
            arcpy.Parameter(
                displayName="Input Polygon",
                name="input_polygon",
                datatype="DEFeatureClass",
                parameterType="Required",
                direction="Input"
            ),
            param,
            arcpy.Parameter(
                displayName="Output Area",
                name="output_area",
                datatype="GPDouble",
                parameterType="Derived",
                direction="Output"
            )
        ]

        return params

    def isLicensed(self):
        return True

    def execute(self, parameters, messages):
        input_polygon = parameters[0].valueAsText
        selected_unit = parameters[1].value

        # Get the spatial reference of the input polygon
        desc = arcpy.Describe(input_polygon)
        spatial_reference = desc.spatialReference

        # Check if spatial reference is defined
        if spatial_reference is not None:
            # Retrieve the linear unit of the spatial reference
            linear_unit = spatial_reference.linearUnitName
            messages.addMessage("Input polygon projection: {}".format(spatial_reference.name))
            messages.addMessage("Selected unit of measurement: {}".format(selected_unit))
        else:
            messages.addWarning("Input polygon does not have a defined projection.")

        # Calculate the area of the input polygon
        with arcpy.da.SearchCursor(input_polygon, ['SHAPE@AREA']) as cursor:
            for row in cursor:
                area = row[0]

        # Convert area to the selected unit of measurement
        if selected_unit == "Square Kilometers":
            area /= 1000000
        elif selected_unit == "Square Miles":
            area /= 2.58999e+6
        elif selected_unit == "Square Feet":
            area *= 10.7639  # 1 Square Meter = 10.7639 Square Feet

        # Set the output parameter value
        parameters[2].value = area


class Toolbox(object):
    def __init__(self):
        # Define toolbox properties
        self.label = "Sample Toolbox"  # Toolbox label
        self.alias = ""  # Toolbox alias

        # List of tool classes associated with this toolbox
        self.tools = [BufferTool, PolygonAreaTool, FieldListerTool]
