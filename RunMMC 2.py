import bpy
import oct2py as op
import numpy as np
import scipy.io
import os
from .utils import get_scene_objs
from .py_props import my_dict, my_list
import platform

class runmmc(bpy.types.Operator):
    bl_label = 'Run MMC'
    bl_description = "Click this button to star MMC!"
    bl_idname = 'a_test.runmmc'
    
    def funrmc(self):
        os.chdir(bpy.utils.user_resource('SCRIPTS', "addons")+'/MMC_in_Blender/Model')
        ## save optical parameters and light source information
        parameters = [] # mu_a, mu_s, n, g
        light_source = [] # location, direction, photon number, Type,

        for obj in bpy.data.objects[0:-1]:
            parameters.append(obj["mu_a"])
            parameters.append(obj["mu_s"])
            parameters.append(obj["n"])
            parameters.append(obj["g"])
        parameters = np.array(parameters)

        obj = bpy.data.objects['light']
        location =  np.array(obj.location)
        direction =  np.array(bpy.context.object.rotation_quaternion)
        light_source.append(obj["nphoton"])
        light_source.append(obj["Type"])
        light_source = np.array(light_source)

        # Save MMC information
        scipy.io.savemat('MMCinfo.mat', mdict={'Optical':parameters, 'light_location':location,'light_direction':direction,'light_info':light_source})

        #run MMC
        oc = op.Oct2Py()
        oc.addpath(oc.genpath(bpy.utils.user_resource('SCRIPTS', "addons")+'/MMC_in_Blender/iso2mesh'))
        system = platform.system()
        if system == 'Windows':
            oc.addpath(oc.genpath(bpy.utils.user_resource('SCRIPTS', "addons")+'/MMC_in_Blender/mmc/Windows/mmc'))
        elif system == 'Darwin':
            oc.addpath(oc.genpath(bpy.utils.user_resource('SCRIPTS', "addons")+'/MMC_in_Blender/mmc/MacOS/mmc'))
        elif system == 'Linux':
            oc.addpath(oc.genpath(bpy.utils.user_resource('SCRIPTS', "addons")+'/MMC_in_Blender/mmc/Linux/mmc'))
        oc.run(bpy.utils.user_resource('SCRIPTS', "addons")+'/MMC_in_Blender/Model/runmmc.m')
        
        #add color to blender model
        

    def execute(self, context):
        print("Int ops--->funivm:")
        self.funrmc()
        print("Utils--->get_scene_objs:")
        get_scene_objs()
        print("Py-Props:")
        print(my_list)
        print(my_dict)
        return {"FINISHED"}
