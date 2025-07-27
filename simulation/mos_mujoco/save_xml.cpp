#include "mujoco.h"
#include <stdio.h>

int main() {
    char error[1000] = "Could not load URDF";
    // 加载模型（自动从URDF转换）
    mjModel* m = mj_loadXML("mos_dog0727.urdf", NULL, error, 1000);
    if (!m) {
        printf("Error loading model: %s\n", error);
        return 1;
    }

    // 保存为 MJCF XML
    if (!mj_saveLastXML("converted.xml", m, NULL, 0)) {
        printf("Failed to save XML.\n");
    } else {
        printf("Saved MJCF as converted.xml\n");
    }

    mj_deleteModel(m);
    return 0;
}
