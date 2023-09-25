import bpy
import sys

# Get the input and output file paths from command line arguments
input_file_path = sys.argv[-2]  # Corrected index
output_file_path = sys.argv[-1]  # Corrected index

# Clear existing data
bpy.ops.wm.read_factory_settings(use_empty=True)

# Load the .obj file
bpy.ops.import_scene.obj(filepath=input_file_path)

# Select all objects in the scene
bpy.ops.object.select_all(action='SELECT')

# Export the scene to .fbx
bpy.ops.export_scene.fbx(filepath=output_file_path, use_selection=True)

print("Conversion complete!")
