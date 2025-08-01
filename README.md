# 四足机器人项目

该项目包含一个四足机器人的完整开发资源,包括仿真、控制算法和远程控制应用.

## 目录结构

*   `docs/`: 项目文档.
*   `simulation/`: 仿真相关文件.
    *   `isaac_sim/`: Isaac Sim仿真环境.
    *   `mujoco/`: MuJoCo仿真环境.
*   `src/`: 机器人控制算法源代码.
    *   `control/`: 核心控制算法.
    *   `utils/`: 通用工具和库.
*   `android_app/`: 安卓遥控应用.

## 开发

### 仿真

*   **Isaac Sim:** 用于进行高保真度的物理仿真和渲染.
*   **MuJoCo:** 用于快速、轻量级的物理仿真.

### 控制算法

控制算法在`src/`目录中开发,主要包括:

*   步态规划
*   平衡控制
*   运动学和动力学

### 安卓应用

安卓应用用于远程控制机器人,功能包括:

*   实时遥测数据显示
*   远程控制指令发送
