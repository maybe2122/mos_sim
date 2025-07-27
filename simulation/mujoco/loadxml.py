import math
import time
import mujoco
import mujoco.viewer
import os
 
#模型路径
model_path = '/home/tjp/Desktop/code/mos_sim/simulation/mujoco/mos_dog.xml'  # 更新为你的模型文件路径
# 加载模型
model = mujoco.MjModel.from_xml_path(model_path) 
# 创建仿真数据 
data = mujoco.MjData(model)
 
if __name__ == "__main__": 
    # 创建仿真和可视化器
    with mujoco.viewer.launch_passive(model, data) as viewer:
        duration = 5000
        start_time = time.time()
        current_time = 0
        while current_time <= duration:
            mujoco.mj_step(model, data)   # 仿真步进
            viewer.sync()                 # 图像同步
            time.sleep(0.01)
            current_time = time.time() - start_time