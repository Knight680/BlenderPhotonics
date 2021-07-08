import bpy
from .ops import Creatregion


class Test_Panel(bpy.types.Panel):
    # 标签
    bl_label = 'a-test'
    bl_idname = 'A_TEST_PL'
    # 面板所属区域
    bl_space_type = "VIEW_3D"
    # 显示面板的地方
    bl_region_type = "UI"
    # 显示面板的地方的归类
    bl_category = "A-TEST"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.operator(Creatregion.bl_idname)
        col.operator(Test_Panel.bl_idname)
