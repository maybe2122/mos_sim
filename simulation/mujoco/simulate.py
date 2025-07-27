import mujoco
import mujoco.viewer
import numpy as np
import time
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))

from control.gait_planner import GaitPlanner
from utils.kinematics import Kinematics

xml = "/home/tjp/Desktop/code/mos_sim/simulation/mujoco/quadruped.xml"

model = mujoco.MjModel.from_xml_path(xml)
data = mujoco.MjData(model)

# Initialize Kinematics and Gait Planner
kinematics = Kinematics(hip_offset=0.05, thigh_length=0.1, calf_length=0.1)
gait_planner = GaitPlanner(step_length=0.1, step_height=0.05, phase_offset=[0.0, 0.5, 0.5, 0.0])

# viewer setup
with mujoco.viewer.launch_passive(model, data) as viewer:
  # Close the viewer automatically after 30 seconds.
  start = time.time()
  while viewer.is_running() and time.time() - start < 30:
    step_start = time.time()

    # Get the current phase in the gait cycle
    phase = (time.time() * 2) % 1.0

    # Calculate desired foot positions for each leg
    for i in range(4):
        foot_pos = gait_planner.get_foot_position(phase, i)
        
        # Calculate inverse kinematics to get joint angles
        joint_angles = kinematics.inverse(foot_pos)
        
        # Set the control signal for the corresponding joints
        for j in range(3):
            data.ctrl[i * 3 + j] = joint_angles[j]

    mujoco.mj_step(model, data)

    viewer.sync()

    time_until_next_step = model.opt.timestep - (time.time() - step_start)
    if time_until_next_step > 0:
      time.sleep(time_until_next_step)