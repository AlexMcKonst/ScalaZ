###!/usr/bin/env python
bl_info = {
    "name": "ScalaZ",
    "author": "Alex McKonst",
    "version": (1, 7, 10),
    "blender": (2, 79, 0),
    "location": "Mesh",
    "warning": "WIP",
    "wiki_url": "https://blenderartists.org/forum/showthread.php?417317-Addon-MASC-this-is-a-set-of-scenarios-for-automating-routine-workflows",
    "tracker_url": "https://github.com/AlexMcKonst/MASC",
    "category": "Mesh"}
import bpy
import os
from bpy.types import Panel, Menu, Group, GroupObjects
from bpy import props
from bpy.props import *

class SclZ(bpy.types.Operator):
    """ScaleZ"""
    bl_idname = "scene.sclz"
    bl_label = "sz"
    bl_options = {"REGISTER", "UNDO"}

    nsz = bpy.props.FloatProperty(name="New height",description="New_height")

    def execute(self, context):
        obj=bpy.context.selected_objects
        CR = bpy.context.space_data.pivot_point
        OR = bpy.context.space_data.transform_orientation
        def scz():
            bpy.data.objects[bpy.context.scene.objects.active.name].dimensions[2] = self.nsz
            szNew = bpy.data.objects[bpy.context.scene.objects.active.name].scale[2]
            bpy.data.objects[bpy.context.scene.objects.active.name].scale.xyz = szNew
        if obj != []:
            if len(bpy.context.selected_objects) >1:
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
                scz()
                bpy.ops.object.select_hierarchy(direction='CHILD', extend=False)
                bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            else:
                scz()
        else:
            self.report({'ERROR'}, 'Please select one or more objects')
        return {"FINISHED"}

    def invoke(self, context, event):
        global nsz
        return context.window_manager.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(SclZ)

def unregister():
    bpy.utils.unregister_class(SclZ)

if __name__ == "__main__":
   register()
