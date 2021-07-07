bl_info = {
    "name": "Run MMC in Blender",
    "author": "Victor",
    "version": (1, 0),  # 插件版本
    "blender": (2, 93, 0),  # 支持blender版本
    "location": "关于插件位于哪个面板的描述 3D视窗+N面板",
    "description": "Modeling in Blender and autorun mmc in Octave",
    "warning": "work with Blender and MMC in Octave. Matlab is not support. Tested on Linux；Save your blender file before using this add-on!",
    "doc_url": "插件的网页链接",
    "tracker_url": "bug 汇报",
    "category": "插件的分类 Object",
}
import bpy
from .ops import Test_Ops
from .ui import Test_Panel


class Test_AddonPref(bpy.types.AddonPreferences):
    bl_idname = __package__
    root: bpy.props.StringProperty(name="Asset root directory",
                                   default="C:/tmp/new_assets",
                                   description="Path to Root Asset Directory",
                                   subtype="DIR_PATH"
                                   )

    def draw(self, context):
        self.layout.row().prop(self, "root", text="预设的根目录")


def register():
    print("Run MMC in Blender installed")
    bpy.utils.register_class(Test_Ops)
    bpy.utils.register_class(Test_Panel)
    bpy.utils.register_class(Test_AddonPref)


def unregister():
    print("Run MMC in Blender uninstalled")
    bpy.utils.unregister_class(Test_AddonPref)
    bpy.utils.unregister_class(Test_Panel)
    bpy.utils.unregister_class(Test_Ops)
