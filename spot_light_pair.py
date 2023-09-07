import maya.cmds as cmds
import time

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

cmds.connectAttr(scale_fc + ".outFloat", spotlight1_transform + ".scaleX")
cmds.connectAttr(scale_fc + ".outFloat", spotlight1_transform + ".scaleY")
cmds.connectAttr(scale_fc + ".outFloat", spotlight1_transform + ".scaleZ")
cmds.connectAttr(scale_fc + ".outFloat", spotlight2_transform + ".scaleX")
cmds.connectAttr(scale_fc + ".outFloat", spotlight2_transform + ".scaleY")
cmds.connectAttr(scale_fc + ".outFloat", spotlight2_transform + ".scaleZ")

# Create float constants for radius
radius_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_radius",
)

# Connect float constants to color temperature attributes of both spotlights
cmds.connectAttr(radius_fc + ".outFloat", spotlight1 + ".aiRadius")
cmds.connectAttr(radius_fc + ".outFloat", spotlight2 + ".aiRadius")

# Create float constants for color temperature
color_temp_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_temp",
)

# Connect float constants to color temperature attributes of both spotlights
cmds.connectAttr(color_temp_fc + ".outFloat", spotlight1 + ".aiColorTemperature")
cmds.connectAttr(color_temp_fc + ".outFloat", spotlight2 + ".aiColorTemperature")

# Create float constants for useColorTemperature
use_color_temp_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_useTemp",
)

# Connect float constants to useColorTemperature attributes of both spotlights
cmds.connectAttr(use_color_temp_fc + ".outFloat", spotlight1 + ".aiUseColorTemperature")
cmds.connectAttr(use_color_temp_fc + ".outFloat", spotlight2 + ".aiUseColorTemperature")

# Create float constant for exposure
exposure_fc = cmds.shadingNode(
    "floatConstant",
    asUtility=True,
    name="floatConstant_" + str(current_time_unix) + "_exposure",
)

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
