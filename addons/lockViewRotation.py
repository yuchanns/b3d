bl_info = {
    "name": "Lock View Rotation",
    "blender": (3, 3, 1),
    "category": "View",
}

import bpy

def draw_lock_rotation(self, context):
    layout = self.layout
    view = context.space_data
    col = layout.column(align=True)
    col.prop(view.region_3d, "lock_rotation", text="Lock View Rotation")

def register():
    bpy.types.VIEW3D_PT_view3d_lock.append(draw_lock_rotation)

def unregister():
    bpy.types.VIEW3D_PT_view3d_lock.remove(draw_lock_rotation)

if __name__ == "__main__":
    register()
