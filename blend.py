import bpy

def mksphere(r):
    s = 2
        
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=s,radius=r)
    bpy.context.selected_objects[0].name = "icosphere_%d" % r
    bpy.ops.export_scene.smd()
    bpy.ops.object.delete()

for i in range(1,6000):
    mksphere(i)
