import bpy
import bmesh
import math

def setupCamera(scene, c):
    pi = math.pi

    scene.camera.rotation_euler[0] = c[0] * (pi / 180.0)
    scene.camera.rotation_euler[1] = c[1] * (pi / 180.0)
    scene.camera.rotation_euler[2] = c[2] * (pi / 180.0)

    scene.camera.location.x = c[3]
    scene.camera.location.y = c[4]
    scene.camera.location.z = c[5]

    return

scene = bpy.data.scenes["Scene"]
view_layer = bpy.context.view_layer


bm = bmesh.new()
bmesh.ops.create_cube(bm, size=2)

mesh = bpy.data.meshes.new('Basic_Cube')
bm.to_mesh(mesh)
mesh.update()
bm.free()

basic_cube = bpy.data.objects.new("Basic_Cube", mesh)
basic_cube.location = (5,5,5)
bpy.context.collection.objects.link(basic_cube)

basic_cube = bpy.data.objects.new("Basic_Cube", mesh)
basic_cube.location = (-5,5,5)
bpy.context.collection.objects.link(basic_cube)


light_data = bpy.data.lights.new(name="New Light", type='POINT')
light_object = bpy.data.objects.new(name="New Light", object_data=light_data)
bpy.context.collection.objects.link(light_object)
light_object.location = (5.0, -5.0, 5.0)

config = list([67.1349, 0.779594, 148.858, 5.57961, 9.16202, 5.34536])

bpy.ops.object.camera_add()
cam = bpy.data.objects['Camera']
cam.rotation_mode = 'XYZ'

scene.camera = cam

setupCamera(scene=scene, c=config)
