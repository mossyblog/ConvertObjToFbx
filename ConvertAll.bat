@echo off
setlocal enabledelayedexpansion
echo Starting the conversion of all OBJ files in the current directory to FBX...
for %%f in (*.obj) do (
    set "name=%%~nf"
    echo Converting %%f to !name!.fbx
    blender --background --python C:\scripts\convert_obj_to_fbx.py -- %%f !name!.fbx
)

echo All conversions complete!
