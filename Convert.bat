@echo off
set INPUT_FILE=%1
set OUTPUT_FILE=%~dpn1.fbx

blender --background --python C:\Scripts\convert_obj_to_fbx.py -- "%INPUT_FILE%" "%OUTPUT_FILE%"
echo Conversion complete!
pause
