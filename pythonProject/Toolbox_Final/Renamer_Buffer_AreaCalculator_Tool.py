
###
# Toolbox Final
###

# For this final project toolbox I decided to use three tools.
# The first tool is a shapefile renamer which allows you to change the name of a shapefile.
# The second is the buffer which runs an analysis on your input shapefile.
# The third tool calculates the area of your input shapefile.


import arcpy

# Define ShapefileRenamerTool class
class ShapefileRenamerTool(object):
    def __init__(self):
        self.label = "Shapefile Renamer Tool"  # Tool label
        self.description = "Rename a shapefile."  # Tool description
        self.canRunInBackground = False  # Set whether the tool can run in the background

    def getParameterInfo(self):
        params = [arcpy.Parameter(displayName="Input Shapefile",
                                  name="input_shapefile",
                                  datatype="DEShapefile",
                                  parameterType="Required",
                                  direction="Input"),
                  arcpy.Parameter(displayName="New Name",
                                  name="new_name",
                                  datatype="GPString",
                                  parameterType="Required",
                                  direction="Input")]
        return params

    def isLicensed(self):
        return True  # Set whether the tool is licensed to execute

    def execute(self, parameters, messages):
        input_shapefile = parameters[0].valueAsText  # Get input shapefile
        new_name = parameters[1].valueAsText          # Get new name

        # Rename the input shapefile with the new name
        arcpy.Rename_management(input_shapefile, new_name)

# Define AreaCalculatorTool class
class AreaCalculatorTool(object):
    def __init__(self):
        self.label = "Area Calculator Tool"  # Tool label
        self.description = "Calculate the area of a feature class."  # Tool description
        self.canRunInBackground = False  # Set whether the tool can run in the background

    def getParameterInfo(self):
        # Define input parameters for the tool
        params = [arcpy.Parameter(displayName="Input Feature",
                                  name="input_feature",
                                  datatype="DEFeatureClass",
                                  parameterType="Required",
                                  direction="Input"),
                  arcpy.Parameter(displayName="Output Unit",
                                  name="output_unit",
                                  datatype="GPString",
                                  parameterType="Optional",
                                  direction="Input",
                                  multiValue=False)]
        params[1].filter.type = "ValueList"
        params[1].filter.list = ["Square Meters", "Acres", "Square Feet"]
        params[1].value = "Square Meters"  # Set default value
        return params

    def isLicensed(self):
        return True  # Set whether the tool is licensed to execute

    def execute(self, parameters, messages):
        input_feature = parameters[0].valueAsText
        output_unit = parameters[1].valueAsText

        # Validate the input unit
        if output_unit not in ["Square Meters", "Acres", "Square Feet"]:
            arcpy.AddError("Invalid output unit specified.")
            return

        # Define a temporary field to store area in square meters
        temp_field = "TEMP_AREA_SQ_M"

        # Calculate area and add it to the feature class
        arcpy.CalculateGeometryAttributes_management(input_feature, [[temp_field, "AREA"]], area_unit="SQUARE_METERS")

        # Retrieve total area
        total_area_sq_m = 0
        with arcpy.da.SearchCursor(input_feature, [temp_field]) as cursor:
            for row in cursor:
                total_area_sq_m += row[0]

        # Convert area to the specified unit
        if output_unit == "Acres":
            total_area = total_area_sq_m / 4046.85642
        elif output_unit == "Square Feet":
            total_area = total_area_sq_m * 10.7639
        else:  # Default to Square Meters
            total_area = total_area_sq_m

        arcpy.AddMessage("Total Area: {} {}".format(total_area, output_unit))

        # Clean up temporary field
        arcpy.DeleteField_management(input_feature, temp_field)


# Define BufferTool class
class BufferTool(object):
    def __init__(self):
        self.label = "Buffer Tool"  # Tool label
        self.description = "Buffer a feature."  # Tool description
        self.canRunInBackground = False  # Set whether the tool can run in the background

    def getParameterInfo(self):
        # Define input parameters for tool
        params = [arcpy.Parameter(displayName="Input Feature",
                                  name="input_feature",
                                  datatype="DEFeatureClass",
                                  parameterType="Required",
                                  direction="Input"),
                  arcpy.Parameter(displayName="Output Feature",
                                  name="output_feature",
                                  datatype="DEFeatureClass",
                                  parameterType="Required",
                                  direction="Output"),
                  arcpy.Parameter(displayName="Buffer Distance",
                                  name="buffer_distance",
                                  datatype="GPLinearUnit",
                                  parameterType="Required",
                                  direction="Input")]  # Change datatype to GPLinearUnit
        return params

    def isLicensed(self):
        return True  # Set whether the tool is licensed to execute

    def execute(self, parameters, messages):
        input_feature = parameters[0].valueAsText   # Get input feature
        output_feature = parameters[1].valueAsText  # Get output feature
        buffer_distance = parameters[2].valueAsText # Get buffer distance
        arcpy.Buffer_analysis(input_feature, output_feature, buffer_distance)


# Define Toolbox class
class Toolbox(object):
    def __init__(self):
        # Define toolbox properties
        self.label = "Sample Toolbox"  # Toolbox label
        self.alias = ""                # Toolbox alias

        # List of tool classes associated with this toolbox
        self.tools = [AreaCalculatorTool, BufferTool, ShapefileRenamerTool]