# doublet.py - simulates 2 cells adhering to each other
# with different balances of cortical tension and cell adhesion

from goo import goo
import bpy

goo.setup_world()
    
# Delete all existing collections 
for collection in bpy.data.collections:  # loop through the existing collection
    # loop through objects in collection
    for objs in collection.objects:
        # delete existing objects in collection 
        bpy.data.objects.remove(objs)
    # Delete collection
    bpy.data.collections.remove(collection)

# Change the Viewport Shading to Rendered
for area in bpy.context.screen.areas: 
    if area.type == 'VIEW_3D':
        for space in area.spaces: 
            if space.type == 'VIEW_3D':
                space.shading.type = 'MATERIAL'

#====================== Colors =========================
# Green
matg = bpy.data.materials.new("Green")
matg.diffuse_color = (0,0.1,0,0.8)
# Red
matr = bpy.data.materials.new("red")
matr.diffuse_color = (0.1,0,0,0.8)

#================== Cell A Collection ==================
# Create a collection for cell A
cA_collection = bpy.data.collections.new("A_Cells")
# link the collection to the scene for visualization 
bpy.context.scene.collection.children.link(cA_collection)
# Define cell A1
cA1 = goo.Cell("cell_A1", loc = (2,2,0))
# Make a Blender mesh object for cell
goo.make_cell(cA1)
# The created cell is the active object
obj = bpy.context.active_object
# Set the object color
obj.active_material = matg
# Remove object from all collections not used in a scene 
# if you do not delete them the object outside colleciton will link to object inside the collection
bpy.ops.collection.objects_remove_all()
# Add the active cell to our specific collection 
bpy.data.collections['A_Cells'].objects.link(obj)

# Define cell A2
cA2 = goo.Cell("cell_A2", loc = (2,-2,0))
# Make a Blender mesh object for cell
goo.make_cell(cA2)
# The created cell is the active object
obj = bpy.context.active_object
# Set the object color
obj.active_material = matg
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all()
# Add the active cell to our specific collection 
bpy.data.collections['A_Cells'].objects.link(obj)

#================== Cell B Collection ==================
# Create a collection for cell B
cB_collection = bpy.data.collections.new("B_Cells")
# link the collection to the scene
bpy.context.scene.collection.children.link(cB_collection)
# Define cell A1
cB1 = goo.Cell("cell_B1", loc = (-2,2,0))
# Make a Blender mesh object for cell
goo.make_cell(cB1)
# The created cell is the active object
obj = bpy.context.active_object
# Set the object color
obj.active_material = matr
# Remove object from all collections not used in a scene 
# if you do not delete them the object outside colleciton will link to object inside the collection
bpy.ops.collection.objects_remove_all()
# Add the active cell to our specific collection 
bpy.data.collections['B_Cells'].objects.link(obj)

# Define cell B2
cB2 = goo.Cell("cell_B2", loc = (-2,-2,0))
# Make a Blender mesh object for cell
goo.make_cell(cB2)
# The created cell is the active object
obj = bpy.context.active_object
# Set the object color
obj.active_material = matr
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all()
# Add the active cell to our specific collection 
bpy.data.collections['B_Cells'].objects.link(obj)

#================== Force A Collection ==================
# Create a collection for force A
fA_collection = bpy.data.collections.new("A_Forces")
# link the collection to the scene 
bpy.context.scene.collection.children.link(fA_collection)
# Define and link force A1
fA1 = goo.Force("force_A1", "cell_A1", -800)
# Make force
goo.make_force(fA1)
# The created force is the active object
obj = bpy.context.active_object
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all()
# Add the active force to our specific collection 
bpy.data.collections['A_Forces'].objects.link(obj)

# Define and link force A2
fA2 = goo.Force("force_A2", "cell_A2", -800)
# Make force
goo.make_force(fA2)
# The created force is the active object
obj = bpy.context.active_object
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all()
# Add the active force to our specific collection 
bpy.data.collections['A_Forces'].objects.link(obj)

#================== Force B Collection ==================
# Create a collection for force B
fB_collection = bpy.data.collections.new("B_Forces")
# link the collection to the scene 
bpy.context.scene.collection.children.link(fB_collection)
# Define and link force B1
fB1 = goo.Force("force_B1", "cell_B1", -800)
# Make force
goo.make_force(fB1)
# The created force is the active object
obj = bpy.context.active_object
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all()
# Add the active force to our specific collection 
bpy.data.collections['B_Forces'].objects.link(obj)

# Define and link force B2
fB2 = goo.Force("force_B2", "cell_B2", -800)
# Make force
goo.make_force(fB2)
# The created force is the active object
obj = bpy.context.active_object
# Remove object from all collections not used in a scene
bpy.ops.collection.objects_remove_all()
# Add the active force to our specific collection 
bpy.data.collections['B_Forces'].objects.link(obj)

# Set the Effector Collection (Select a cell then go to
# Physics Properties > Cloth > Field Weights > Effector Collection > selct the force collection)
for collection in bpy.data.collections:
    
    # Exclude the objects in the force collections
    if 'Cells' in collection.name_full:
        # Collection name
        coll_name = collection.name_full
        # Save the word before the underscore
        force_name = coll_name[0:coll_name.find('_')] + '_Forces'
        # Loop through the objects existed in the collection 
        for obj in collection.objects:
            # Cloth > Effector collection
            obj.modifiers['Cloth'].settings.effector_weights.collection = bpy.data.collections[force_name]
            # Cloth
            obj.modifiers['Cloth'].settings.quality = 6
            obj.modifiers['Cloth'].settings.air_damping = 5
            obj.modifiers['Cloth'].settings.bending_model = 'ANGULAR'
            # Cloth > Stiffness 
            obj.modifiers['Cloth'].settings.tension_stiffness = 1
            obj.modifiers['Cloth'].settings.compression_stiffness = 1
            obj.modifiers['Cloth'].settings.shear_stiffness = 1
            obj.modifiers['Cloth'].settings.bending_stiffness = 1
            # Cloth > Damping
            obj.modifiers['Cloth'].settings.tension_damping = 25
            obj.modifiers['Cloth'].settings.compression_damping = 25
            obj.modifiers['Cloth'].settings.shear_damping = 25
            obj.modifiers['Cloth'].settings.bending_damping = 0.5
            # Cloth > Internal Springs
            obj.modifiers['Cloth'].settings.use_internal_springs = True
            obj.modifiers['Cloth'].settings.internal_spring_max_length = 0
            obj.modifiers['Cloth'].settings.internal_spring_max_diversion = 0.785398
            obj.modifiers['Cloth'].settings.internal_spring_normal_check = True
            obj.modifiers['Cloth'].settings.internal_tension_stiffness = 1
            obj.modifiers['Cloth'].settings.internal_compression_stiffness = 1
            obj.modifiers['Cloth'].settings.internal_tension_stiffness_max = 5
            obj.modifiers['Cloth'].settings.internal_compression_stiffness_max = 5
            # Cloth > Pressure
            obj.modifiers['Cloth'].settings.uniform_pressure_force = 5
            obj.modifiers['Cloth'].settings.use_pressure_volume = True
            obj.modifiers['Cloth'].settings.target_volume = 1
            obj.modifiers['Cloth'].settings.pressure_factor = 1
            obj.modifiers['Cloth'].settings.fluid_density = 0
            # Cloth > Collisions
            obj.modifiers['Cloth'].collision_settings.collision_quality = 6
            obj.modifiers['Cloth'].collision_settings.use_collision = True
            obj.modifiers['Cloth'].collision_settings.use_self_collision = True
            obj.modifiers['Cloth'].collision_settings.self_friction = 5
            obj.modifiers['Cloth'].collision_settings.self_distance_min = 0.015
            obj.modifiers['Cloth'].collision_settings.self_impulse_clamp = 0
            # Collision
            obj.modifiers['Collision'].settings.damping = 0.579821
            obj.modifiers['Collision'].settings.thickness_outer = 0.02
            obj.modifiers['Collision'].settings.thickness_inner = 0.2
            obj.modifiers['Collision'].settings.cloth_friction = 5
            obj.modifiers['Collision'].settings.use_culling = True
            
handlers = goo.handler_class()
handlers.forces = [fA1, fA2, fB1, fB2]
bpy.app.handlers.frame_change_post.clear()
bpy.app.handlers.frame_change_post.append(handlers.adhesion_handler)
