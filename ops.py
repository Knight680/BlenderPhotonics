import bpy
import oct2py as op
import numpy as np
import scipy.io
import os
from .utils import get_scene_objs
from .py_props import my_dict, my_list


class Creatregion(bpy.types.Operator):
    bl_label = 'genert volumatic mesh'
    bl_description = "这是一个可以移动物体的按钮"
    bl_idname = 'a_test.creatregion'

    # 可以让操作执行后左下角显示一个提示

    bl_options = {"REGISTER", "UNDO"}
    keepratio: bpy.props.FloatProperty(default=1.0,name="ratio keep for volum mesh(0-1)")
    maxvolum: bpy.props.FloatProperty(default=100.0, name="Max_tetrahedraw_volum")

    def func(self):
        obj = bpy.context.view_layer.objects.active
        #jioned
        bpy.ops.object.select_all(action='SELECT')
        if len(bpy.context.selected_objects)>=2:
            bpy.ops.object.join()

        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.intersect(mode='SELECT', separate_mode='NONE', solver='EXACT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
        bpy.ops.object.editmode_toggle()

        #output mesh data to Octave
        # this works only in object mode,
        verts = [vert.co for vert in obj.data.vertices]
        edges = [edge.vertices[:] for edge in obj.data.edges]
        faces = [face.vertices[:] for face in obj.data.polygons]
        v = np.array(verts)
        f = np.array(faces)

        print("="*40) # printing marker

        oc = op.Oct2Py()
        oc.addpath(oc.genpath('/Users/knight/model/iso2mesh'))

        v = np.array(verts)
        f = np.array(faces)

        # Save file
        scipy.io.savemat('result.mat', mdict={'v':v, 'f':f, 'ratio':self.keepratio, 'maxv':self.maxvolum})
        oc.run('/Users/knight/model/demo_blender.m')

    def execute(self, context):
        print("Int ops--->func:")
        self.func()
        print("Utils--->get_scene_objs:")
        get_scene_objs()
        print("Py-Props:")
        print(my_list)
        print(my_dict)
        return {"FINISHED"}
