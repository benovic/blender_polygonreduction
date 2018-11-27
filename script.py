import bpy

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            print(obj.name)
            bpy.context.scene.objects.active = obj
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.quads_convert_to_tris()
            bpy.ops.mesh.remove_doubles()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.tris_convert_to_quads()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.delete_loose()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.face_make_planar()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.dissolve_limited()   
            bpy.ops.mesh.dissolve_limited(angle_limit=0.261799)
            bpy.ops.object.editmode_toggle()