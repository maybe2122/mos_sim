import numpy as np

class Kinematics:
    def __init__(self, hip_offset, thigh_length, calf_length):
        self.hip_offset = hip_offset
        self.thigh_length = thigh_length
        self.calf_length = calf_length

    def forward(self, q):
        """
        Calculates the forward kinematics for a single leg.
        q: array of 3 joint angles [hip, thigh, calf]
        Returns: 3D position of the foot relative to the hip attachment point.
        """
        hip_angle, thigh_angle, calf_angle = q

        x = self.hip_offset * np.cos(hip_angle) - \
            self.thigh_length * np.sin(thigh_angle) * np.sin(hip_angle) - \
            self.calf_length * np.sin(thigh_angle + calf_angle) * np.sin(hip_angle)

        y = self.hip_offset * np.sin(hip_angle) + \
            self.thigh_length * np.sin(thigh_angle) * np.cos(hip_angle) + \
            self.calf_length * np.sin(thigh_angle + calf_angle) * np.cos(hip_angle)

        z = -self.thigh_length * np.cos(thigh_angle) - \
            self.calf_length * np.cos(thigh_angle + calf_angle)

        return np.array([x, y, z])

    def inverse(self, p):
        """
        Calculates the inverse kinematics for a single leg.
        p: 3D position of the foot relative to the hip attachment point.
        Returns: array of 3 joint angles [hip, thigh, calf]
        """
        x, y, z = p

        # Hip angle
        hip_angle = np.arctan2(y, x)

        # Calf angle
        d = np.sqrt(x**2 + y**2 + z**2)
        alpha = np.arccos((self.thigh_length**2 + self.calf_length**2 - d**2) / (2 * self.thigh_length * self.calf_length))
        calf_angle = np.pi - alpha

        # Thigh angle
        beta = np.arccos((self.thigh_length**2 + d**2 - self.calf_length**2) / (2 * self.thigh_length * d))
        gamma = np.arctan2(-z, np.sqrt(x**2 + y**2))
        thigh_angle = beta + gamma

        return np.array([hip_angle, thigh_angle, calf_angle])