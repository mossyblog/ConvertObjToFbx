# OBJ to FBX Converter

This repository contains scripts and instructions for converting 3D model files from OBJ format to FBX format using Blender. The converter can be used through command-line batch files and also integrated into Windows File Explorer's context menu for easy access.

## Contents

1. [convert_obj_to_fbx.py](./convert_obj_to_fbx.py) - Python script to be run with Blender for performing the conversion.
2. [Convert.bat](./Convert.bat) - Batch file for converting a single OBJ file to FBX.
3. [ConvertAll.bat](./ConvertAll.bat) - Batch file for converting all OBJ files in the current directory to FBX.
4. Registry Modification - Instructions for adding a "Convert to FBX" option to the context menu for OBJ files in Windows File Explorer.

## Usage

### Convert.bat

To convert a single OBJ file to FBX, run the `Convert.bat` file with the following syntax:

```sh
Convert.bat path\to\input.obj 
```
Each OBJ file will be converted to an FBX file with the same name in the same directory.

### convert_obj_to_fbx.py
To add a "Convert to FBX" option to the context menu for OBJ files in Windows File Explorer, follow the instructions provided in the ConvertReg.reg file. This will modify the Windows Registry to integrate the converter into the context menu.

** _Note: Modifying the Windows Registry can affect system behavior. Please follow the instructions carefully and consider backing up the registry before making changes._ **

### License
This project is licensed under the MIT License




