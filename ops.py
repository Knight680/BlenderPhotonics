import bpy
import oct2py as op
import numpy as np
import scipy.io
import os
from .utils import get_scene_objs
from .py_props import my_dict, my_list


class Creat_volum_mesh_from_your_creat(bpy.types.Operator):
    bl_label = 'Tetrahedralize your creations'
    bl_description = "This button could tetrahedralize your creations"
    bl_idname = 'a_test.test_ops'

    # 可以让操作执行后左下角显示一个提示

    bl_options = {"REGISTER", "UNDO"}
    Keepratio: bpy.props.FloatProperty(default=1,name="ratio keep for volum mesh(0-1)")
    Maxvolum: bpy.props.FloatProperty(default=100, name="Max_tetrahedraw_volum")

    def func(self):
        for o in bpy.context.selected_objects:
            if self.move_axis == "X":
                o.location.x += self.move_step
            elif self.move_axis == "Y":
                o.location.y += self.move_step
            else:
                o.location.z += self.move_step

    def execute(self, context):
        print("Int ops--->func:")
        self.func()
        print("Utils--->get_scene_objs:")
        get_scene_objs()
        print("Py-Props:")
        print(my_list)
        print(my_dict)
        return {"FINISHED"}
