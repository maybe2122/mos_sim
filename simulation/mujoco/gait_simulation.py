import mujoco
import mujoco.viewer
import numpy as np
import time

# Load the MuJoCo model
xml_path = "mos_dog.xml" # Assuming this script is in the same directory as mos_dog.xml
model = mujoco.MjModel.from_xml_path(xml_path)
data = mujoco.MjData(model)

# Setup viewer
viewer = mujoco.viewer.MjViewer(model, data)

# Define joint names from your mos_dog.xml
joint_names = [
    "6",
    "font_gear",
]

# Get joint IDs
joint_ids = [model.joint(name).id for name in joint_names]

# Control parameters
amplitude_joint_6 = 0.5  # radians
amplitude_font_gear = 1.0 # radians
frequency = 1.0      # Hz
time_step = model.opt.timestep

# Simulation loop
t = 0
while viewer.is_running():
    # Calculate desired joint positions based on simple sinusoidal motion
    # Joint '6'
    if "6" in joint_names:
        joint_6_id = model.joint("6").id
        data.ctrl[joint_6_id] = amplitude_joint_6 * np.sin(2 * np.pi * frequency * t)

    # Joint 'font_gear'
    if "font_gear" in joint_names:
        font_gear_id = model.joint("font_gear").id
        data.ctrl[font_gear_id] = amplitude_font_gear * np.sin(2 * np.pi * frequency * t + np.pi/2) # Add a phase offset

    # Step the simulation
    mujoco.mj_step(model, data)

    # Update viewer
    viewer.render()

    # Advance time
    t += time_step

    # Optional: Add a small delay to control simulation speed if it runs too fast
    # time.sleep(time_step)

viewer.close()