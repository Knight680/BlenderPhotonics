import bpy

class Test_AddonP(bpy.types.AddonPreferences):
    bl_idname = 'a_test.Test_AddonPref'
    mystl = bpy.props.StringProperty(subtype="DIR_PATH",default=bpy.utils.user_resource('SCRIPTS', "addons"))
    bpy.types.Scene.mystl = mystl
