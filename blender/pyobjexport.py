# THIS SCRIPT CAN BE IMPORTED INTO BLENDER TO EXPORT ANY OBJECT AS A .pyobj
# THIS IS HOW I ACHIEVED GETTING SHAPES LIKE THE BALL AND THE MONKEY
# BASED ON BLENDER TEMPLATE

import bpy
from mathutils import Vector

def write_some_data(context, filepath):
    print("running write_some_data...")
    output = ["c[255,255,255]\n"]

    o = context.object
    local_bbox_center = 0.125 * sum((Vector(b) for b in o.bound_box), Vector())
    global_bbox_center = o.matrix_world @ local_bbox_center

    output.append(f"o[{global_bbox_center.x}, {global_bbox_center.z}, {global_bbox_center.y - 2}]\n")

    verts_co = [v.co for v in o.data.vertices]

    for v in verts_co:
        output.append(f"v[{v.x}, {v.z}, {v.y - 2}]\n")

    faces = o.data.polygons

    for face in faces:
        result = "f0["
        for v in face.vertices:
            result += str(v) + ", "
        result = result[:len(result) - 2] + "]"
        result += f"[{face.normal.x}, {face.normal.z}, {face.normal.y}]\n"
        output.append(result)


    f = open(filepath, 'w', encoding='utf-8')
    f.writelines(output)
    f.close()

    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export.pyobj"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export To pyobj"

    # ExportHelper mix-in class uses this.
    filename_ext = ".pyobj"

    filter_glob: StringProperty(
        default="*.pyobj",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        return write_some_data(context, self.filepath)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="pyobj")


# Register and add to the "file selector" menu (required to use F3 search "Text Export Operator" for quick access).
def register():
    bpy.utils.register_class(ExportSomeData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()
