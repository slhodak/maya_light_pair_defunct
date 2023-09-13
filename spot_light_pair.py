import maya.cmds as cmds
import time


####                      ####
# x# Part 1. SpotLight Pair ###
####                      ####

# Create two spotlights and name them based on current Unix time
current_time_unix = int(time.time())
spotlight1_name = "spotlight_" + str(current_time_unix) + "_1"
spotlight2_name = "spotlight_" + str(current_time_unix) + "_2"
spotlight1 = cmds.spotLight(name=spotlight1_name)
spotlight2 = cmds.spotLight(name=spotlight2_name)

spotlight1_transform = cmds.listRelatives(spotlight1, parent=True)
if spotlight1_transform:
    spotlight1_transform = spotlight1_transform[0]

spotlight2_transform = cmds.listRelatives(spotlight2, parent=True)
if spotlight2_transform:
    spotlight2_transform = spotlight2_transform[0]

# Create float constant for spotlight scales
# Connect float constants to scale X, Y, and Z attributes of both spotlights
scale_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_scale",
)

for scale_property in [".scaleX", ".scaleY", ".scaleZ"]:
    cmds.connectAttr(scale_fc + ".outFloat", spotlight1_transform + scale_property)
    cmds.connectAttr(scale_fc + ".outFloat", spotlight2_transform + scale_property)

# Create float constants for radius
radius_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_radius",
)

# Connect float constants to radius attributes of both spotlights
cmds.connectAttr(radius_fc + ".outFloat", spotlight1 + ".aiRadius")
cmds.connectAttr(radius_fc + ".outFloat", spotlight2 + ".aiRadius")

# Create float constants for cone angle
cone_angle_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_cone_angle",
)
cmds.setAttr(cone_angle_fc + ".inFloat", 20)

# Connect float constants to cone angle attributes of both spotlights
cmds.connectAttr(cone_angle_fc + ".outFloat", spotlight1 + ".coneAngle")
cmds.connectAttr(cone_angle_fc + ".outFloat", spotlight2 + ".coneAngle")

# Create float constants for penumbra angle
penumbra_angle_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_penumbra_angle",
)
cmds.setAttr(penumbra_angle_fc + ".inFloat", 0)

# Connect float constants to penumbra angle attributes of both spotlights
cmds.connectAttr(penumbra_angle_fc + ".outFloat", spotlight1 + ".penumbraAngle")
cmds.connectAttr(penumbra_angle_fc + ".outFloat", spotlight2 + ".penumbraAngle")

# Create float constants for color temperature
color_temp_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_temp",
)
cmds.setAttr(color_temp_fc + ".inFloat", 5500)

# Connect float constants to color temperature attributes of both spotlights
cmds.connectAttr(color_temp_fc + ".outFloat", spotlight1 + ".aiColorTemperature")
cmds.connectAttr(color_temp_fc + ".outFloat", spotlight2 + ".aiColorTemperature")

# Create float constants for useColorTemperature
use_color_temp_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_useTemp",
)
cmds.setAttr(use_color_temp_fc + ".inFloat", 1)

# Connect float constants to useColorTemperature attributes of both spotlights
cmds.connectAttr(use_color_temp_fc + ".outFloat", spotlight1 + ".aiUseColorTemperature")
cmds.connectAttr(use_color_temp_fc + ".outFloat", spotlight2 + ".aiUseColorTemperature")

# Create float constant for exposure
exposure_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_exposure",
)
cmds.setAttr(exposure_fc + ".inFloat", 8)

# Connect float constants to exposure attributes of both spotlights
cmds.connectAttr(exposure_fc + ".outFloat", spotlight1 + ".aiExposure")
cmds.connectAttr(exposure_fc + ".outFloat", spotlight2 + ".aiExposure")

# Create a color constant
color_constant = cmds.shadingNode(
    "colorConstant",
    asUtility=True,
    name="colorConstant_" + str(current_time_unix) + "_color",
)

# Connect color constant to color attributes of both spotlights
cmds.connectAttr(color_constant + ".outColor", spotlight1 + ".color")
cmds.connectAttr(color_constant + ".outColor", spotlight2 + ".color")

# Connect to all RGB as well
for rgb_channel in ["R", "G", "B"]:
    cmds.connectAttr(
        color_constant + f".outColor{rgb_channel}", spotlight1 + f".color{rgb_channel}"
    )
    cmds.connectAttr(
        color_constant + f".outColor{rgb_channel}", spotlight2 + f".color{rgb_channel}"
    )


####          ####
### Part 2: UI ###
####          ####


# Function to update spotlight attributes
def update_spotlight_attributes(*args):
    # Get the values from UI elements
    scale_value = cmds.floatSliderGrp(scale_slider, query=True, value=True)
    radius_value = cmds.floatSliderGrp(radius_slider, query=True, value=True)
    cone_angle_value = cmds.floatSliderGrp(cone_angle_slider, query=True, value=True)
    penumbra_angle_value = cmds.floatSliderGrp(
        penumbra_angle_slider, query=True, value=True
    )
    color_temp_value = cmds.floatSliderGrp(color_temp_slider, query=True, value=True)
    exposure_value = cmds.floatSliderGrp(exposure_slider, query=True, value=True)
    use_color_temp_value = cmds.checkBox(
        use_color_temp_checkbox, query=True, value=True
    )
    # color_value = cmds.colorSliderGrp(color_slider, query=True, rgb=True)

    # Apply the values to the shared attributes
    cmds.setAttr(scale_fc + ".inFloat", scale_value)
    cmds.setAttr(radius_fc + ".inFloat", radius_value)
    cmds.setAttr(cone_angle_fc + ".inFloat", cone_angle_value)
    cmds.setAttr(penumbra_angle_fc + ".inFloat", penumbra_angle_value)
    cmds.setAttr(color_temp_fc + ".inFloat", color_temp_value)
    cmds.setAttr(exposure_fc + ".inFloat", exposure_value)
    cmds.setAttr(use_color_temp_fc + ".inFloat", use_color_temp_value)
    # cmds.setAttr(spotlight + ".color", color_value[0], color_value[1], color_value[2], type="double3")


# Create a window
if cmds.window("spotlightAttributesWindow", exists=True):
    cmds.deleteUI("spotlightAttributesWindow", window=True)

window = cmds.window(
    "spotlightAttributesWindow", title="Spotlight Attributes", widthHeight=(300, 400)
)

# Create a form layout
form_layout = cmds.formLayout(parent=window)

# Create UI elements with sliders
scale_slider = cmds.floatSliderGrp(
    label="Scale",
    field=True,
    minValue=0.1,
    maxValue=10.0,
    value=1.0,
    fieldMinValue=0.1,
    fieldMaxValue=10.0,
    step=0.1,
    precision=2,
    changeCommand=update_spotlight_attributes,
)
radius_slider = cmds.floatSliderGrp(
    label="Radius",
    field=True,
    minValue=0.1,
    maxValue=10.0,
    value=1.0,
    fieldMinValue=0.1,
    fieldMaxValue=10.0,
    step=0.1,
    precision=2,
    changeCommand=update_spotlight_attributes,
)
cone_angle_slider = cmds.floatSliderGrp(
    label="Cone Angle",
    field=True,
    minValue=1.0,
    maxValue=180.0,
    value=20.0,
    fieldMinValue=1.0,
    fieldMaxValue=180.0,
    step=1.0,
    precision=0,
    changeCommand=update_spotlight_attributes,
)
penumbra_angle_slider = cmds.floatSliderGrp(
    label="Penumbra Angle",
    field=True,
    minValue=0.0,
    maxValue=90.0,
    value=0.0,
    fieldMinValue=0.0,
    fieldMaxValue=90.0,
    step=1.0,
    precision=0,
    changeCommand=update_spotlight_attributes,
)
color_temp_slider = cmds.floatSliderGrp(
    label="Color Temperature",
    field=True,
    minValue=1000.0,
    maxValue=10000.0,
    value=5500.0,
    fieldMinValue=1000.0,
    fieldMaxValue=10000.0,
    step=100,
    precision=0,
    changeCommand=update_spotlight_attributes,
)
exposure_slider = cmds.floatSliderGrp(
    label="Exposure",
    field=True,
    minValue=-10.0,
    maxValue=10.0,
    value=8.0,
    fieldMinValue=-10.0,
    fieldMaxValue=10.0,
    step=0.1,
    precision=1,
    changeCommand=update_spotlight_attributes,
)

use_color_temp_checkbox = cmds.checkBox(
    label="Use Color Temperature", value=True, changeCommand=update_spotlight_attributes
)

# Arrange UI elements in the form layout
cmds.formLayout(
    form_layout,
    edit=True,
    attachForm=[
        (scale_slider, "left", 10),
        (scale_slider, "top", 10),
        (radius_slider, "left", 10),
        (radius_slider, "top", 50),
        (cone_angle_slider, "left", 10),
        (cone_angle_slider, "top", 90),
        (penumbra_angle_slider, "left", 10),
        (penumbra_angle_slider, "top", 130),
        (color_temp_slider, "left", 10),
        (color_temp_slider, "top", 170),
        (exposure_slider, "left", 10),
        (exposure_slider, "top", 210),
        (use_color_temp_checkbox, "left", 10),
        (use_color_temp_checkbox, "top", 250),
        # (color_slider, 'left', 10), (color_slider, 'top', 290),
    ],
)

# Show the window
cmds.showWindow(window)

# Initialize the UI with the current values
cmds.floatSliderGrp(scale_slider, edit=True, value=1.0)
cmds.floatSliderGrp(radius_slider, edit=True, value=1.0)
cmds.floatSliderGrp(cone_angle_slider, edit=True, value=20.0)
cmds.floatSliderGrp(penumbra_angle_slider, edit=True, value=0.0)
cmds.floatSliderGrp(color_temp_slider, edit=True, value=5500.0)
cmds.floatSliderGrp(exposure_slider, edit=True, value=8.0)
cmds.checkBox(use_color_temp_checkbox, edit=True, value=1)
# cmds.colorSliderGrp(color_slider, edit=True, rgb=(1.0, 1.0, 1.0))
