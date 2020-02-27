# RIG LAYERS UI SCRIPT FOR BLENDER 2.8
# This script builds off of a youtube tutorial you can find here: 
# https://www.youtube.com/watch?v=TsXglw6eD3U
#
# Author: Moses Molina
#
# Description:  Creates a custom UI panel to toggle bone layer visibility.
#               The advantage over the existing toggles in the armature is 
#               the ability to name the layers.
#
# Usage:        Use a proper bone naming convention and put bones into 
#               desired bone layers. Then, run this script to create a 
#               custom visibility toggle panel.
#
# Notes:        This script essentially just polls each bone layer and names 
#               the layer after the first bone it finds. Layer[0] should be
#               the root bone, but does not have to be.
#
import bpy

class RigLayers(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Rig Layers"
    bl_category = "View"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        #Find the armature
        for ob in bpy.data.objects:
            if ob.type == 'ARMATURE':
                armature = ob.data
    
                #Add root layer to the UI
                row = col.row()
                row.prop(armature, 'layers', index=0, toggle=True, text='Root')
                row = col.row()
    
                #Used to create a new row every two layers
                cnt = 0
    
                #For each bone layer find a bone that exists in it and then name the layer after it.
                for i in range(1, 32):
                    layerName = ''
                    for bone in armature.bones:
                        if(bone.layers[i]):
                            cnt = cnt + 1
                            layerName = bone.name
                            row.prop(armature, 'layers', index=i, toggle=True, text=layerName)
                            if cnt == 2:
                                row = col.row()
                                cnt = 0
                            break
    
bpy.utils.register_class(RigLayers)