bl_info = {
    "name": "Quality of Life",
    "blender": (2, 80, 0),
    "category": "DOR",
}

import bpy,bmesh
import os
import shutil
import datetime

class SaveSnapshotOperator(bpy.types.Operator):
    bl_idname = "object.save_snapshot_operator"
    bl_label = "Save Snapshot"
    bl_description = "Save a snapshot of the current file"

    def execute(self, context):
        print("Snapshotting")
        user_preferences = bpy.context.preferences
        addon_prefs = user_preferences.addons[__name__].preferences

        if not bpy.data.is_saved:
            print("File not saved yet, skipping snapshot")
            return {'FINISHED'}

        filepath = bpy.data.filepath
        blend_dir = os.path.dirname(filepath)

        if not blend_dir:
            print("Unable to determine the .blend file's directory, skipping snapshot")
            return {'FINISHED'}

        filename, extension = os.path.splitext(os.path.basename(filepath))

        # Create a subfolder named ".Snapshots" if it doesn't exist
        snapshots_dir = os.path.join(blend_dir, "Snapshots")
        os.makedirs(snapshots_dir, exist_ok=True)

        # Format the timestamp as dayMMMyy-HHMM
        timestamp = datetime.datetime.now().strftime('%d%b%y-%H%M')
        snapshot_name = f"{filename}-{timestamp}{extension}"

        snapshot_path = os.path.join(snapshots_dir, snapshot_name)

        shutil.copy2(filepath, snapshot_path)
        print(f"Snapshot taken and stored at {snapshot_path}")

        return {'FINISHED'}

class MoveVerticesToXZeroOperator(bpy.types.Operator):
    bl_idname = "object.move_vertices_to_x_zero"
    bl_label = "Zero X Axis"
    bl_description = "Move all selected vertices to X=0"
    
    print(f"Moving")

    def execute(self, context):
        mode = bpy.context.active_object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        for vert in selectedVerts:
            new_location = vert.co
            new_location[0] = 0 
            new_location[1] = new_location[1]
            new_location[2] = new_location[2]
            vert.co = new_location
            print("Moving: " + str(vert))
            
        bpy.ops.object.mode_set(mode=mode)
        return {'FINISHED'}

class DeleteVerticesToRightOperator(bpy.types.Operator):
    bl_idname = "object.delete_vertices_to_right"
    bl_label = "Del Rightside"
    bl_description = "Delete all vertices to the right of the X=0 plane"    

    def execute(self, context):
        obj = bpy.context.active_object
        mode = bpy.context.active_object.mode        
        if obj and obj.type == 'MESH':
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')    
            selectedVerts = [v for v in obj.data.vertices]
            bpy.ops.object.mode_set(mode = 'EDIT') 
            bpy.ops.mesh.select_mode(type="VERT")
            mesh = bmesh.from_edit_mesh(obj.data)
            for v in mesh.verts:
                 if v.co.x > 0:
                     v.select = True
                 else:
                    v.select = False
            
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.dissolve_verts()
            bpy.ops.mesh.delete(type='VERT')
            bpy.ops.object.mode_set(mode='OBJECT') 

            obj.data.update()
            bpy.context.view_layer.update()
        return {'FINISHED'}

class CustomSidebarTabOperator(bpy.types.Operator):
    bl_idname = "object.custom_sidebar_tab_operator"
    bl_label = "Merge Obj"
    bl_description = "This is a custom button in the sidebar tab"

    def execute(self, context):
        # Your custom operator logic here
        print("Custom button clicked")
        return {'FINISHED'}

class CustomSidebarTabPanel(bpy.types.Panel):
    bl_label = "Custom Sidebar Tab"
    bl_idname = "PT_Custom_Sidebar_Tab"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'  # Add the tab to the "Tool" shelf

    def draw(self, context):
        layout = self.layout

        # Button for saving a snapshot
        layout.operator("object.save_snapshot_operator")

        # Button for moving selected vertices to X=0
        layout.operator("object.move_vertices_to_x_zero")

        # Button for deleting vertices to the right of the mirror
        layout.operator("object.delete_vertices_to_right")

        # Your custom button here (if needed)
        layout.operator("object.custom_sidebar_tab_operator")

def save_snapshot(dummy):
    user_preferences = bpy.context.preferences
    addon_prefs = user_preferences.addons[__name__].preferences

    if not bpy.data.is_saved:
        print("File not saved yet, skipping snapshot")
        return

    filepath = bpy.data.filepath
    blend_dir = os.path.dirname(filepath)

    if not blend_dir:
        print("Unable to determine the .blend file's directory, skipping snapshot")
        return

    filename, extension = os.path.splitext(os.path.basename(filepath))

    # Create a subfolder named ".Snapshots" if it doesn't exist
    snapshots_dir = os.path.join(blend_dir, "Snapshots")
    os.makedirs(snapshots_dir, exist_ok=True)

    # Format the timestamp as dayMMMyy-HHMM
    timestamp = datetime.datetime.now().strftime('%d%b%y-%H%M')
    snapshot_name = f"{filename}-{timestamp}{extension}"

    snapshot_path = os.path.join(snapshots_dir, snapshot_name)

    shutil.copy2(filepath, snapshot_path)
    print(f"Snapshot taken and stored at {snapshot_path}")

def register():
    bpy.utils.register_class(SaveSnapshotOperator)
    bpy.utils.register_class(MoveVerticesToXZeroOperator)
    bpy.utils.register_class(DeleteVerticesToRightOperator)
    bpy.utils.register_class(CustomSidebarTabOperator)
    bpy.utils.register_class(CustomSidebarTabPanel)
    bpy.app.handlers.save_post.append(SaveSnapshotOperator)

def unregister():
    bpy.utils.unregister_class(SaveSnapshotOperator)
    bpy.utils.unregister_class(MoveVerticesToXZeroOperator)
    bpy.utils.unregister_class(DeleteVerticesToRightOperator)
    bpy.utils.unregister_class(CustomSidebarTabOperator)
    bpy.utils.unregister_class(CustomSidebarTabPanel)
    bpy.app.handlers.save_post.remove(SaveSnapshotOperator)

if __name__ == "__main__":
    register()
