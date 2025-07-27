from omni.isaac.kit import SimulationApp

# This is a basic example of how to load a URDF file into Isaac Sim.
# For more advanced usage, please refer to the Isaac Sim documentation.

CONFIG = {
    "renderer": "RayTracedLighting",
    "headless": False,
}

simulation_app = SimulationApp(CONFIG)

import omni.usd
from omni.isaac.core import World
from omni.isaac.core.robots import Robot
from omni.isaac.core.utils.prims import create_prim
from omni.isaac.core.utils.nucleus import get_assets_root_path

# Create a new stage
stage = omni.usd.get_context().new_stage()

# Create a world
world = World(stage=stage)

# Add a ground plane
assets_root_path = get_assets_root_path()
if assets_root_path is None:
    print("Could not find Isaac Sim assets folder")
else:
    asset_path = assets_root_path + "/Isaac/Environments/Simple_Room/simple_room.usd"
    create_prim(prim_path="/World/simple_room", prim_type="Xform", usd_path=asset_path)

# Load the robot from the URDF file
robot = world.scene.add(
    Robot(
        prim_path="/World/quadruped",
        name="quadruped",
        usd_path="/home/tjp/Desktop/code/mos_sim/simulation/isaac_sim/quadruped.urdf",
        position=[0, 0, 0.5],
    )
)

# Add the world to the simulation
world.reset()

# Run the simulation
while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
