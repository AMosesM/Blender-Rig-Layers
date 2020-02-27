# Blender-Rig-Layers
### Author: Moses Molina

## Description
Blender python script that creates a custom UI panel to toggle bone layer visibility. The advantage over the existing toggles in the armature is the ability to name the layers.

## Usage
Use a proper bone naming convention and put bones into desired bone layers. Then, run this script to create a custom visibility toggle panel.

## Notes:        
This script essentially just polls each bone layer and names the layer after the first bone it finds. Layer[0] should be the root bone, but does not have to be.
