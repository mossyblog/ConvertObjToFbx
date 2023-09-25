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


## Blender Setup

Before using the scripts, ensure that Blender is installed on your system and correctly set up in your system's PATH. This allows the scripts to invoke Blender from the command line.

### Steps to Add Blender to PATH:

1. **Find Blender Executable:**
   - Locate the directory where Blender is installed. The Blender executable (`blender.exe`) is usually located in the installation directory.

2. **Edit System Environment Variables:**
   - Right-click on 'This PC' or 'Computer' on your desktop or in File Explorer, and select 'Properties'.
   - Click on 'Advanced system settings' on the left.
   - In the System Properties window, click on the 'Environment Variables...' button.

3. **Add Blender to PATH:**
   - In the Environment Variables window, under 'System variables', scroll down and select the 'Path' variable, then click on 'Edit...'.
   - In the Edit Environment Variable window, click 'New' and paste the path to the directory containing `blender.exe`.
   - Click 'OK' to close each window.

4. **Verify Blender Setup:**
   - Open a new Command Prompt window.
   - Type `blender --version` and press Enter. If Blender is correctly set up, it will display the installed Blender version.

Once Blender is correctly set up in your system's PATH, you should be able to use the conversion scripts provided in this repository.


