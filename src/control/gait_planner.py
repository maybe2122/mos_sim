import numpy as np

class GaitPlanner:
    def __init__(self, step_length, step_height, phase_offset):
        self.step_length = step_length
        self.step_height = step_height
        self.phase_offset = phase_offset

    def get_foot_position(self, phase, leg_index):
        """
        Calculates the desired foot position for a given leg and phase.
        phase: value between 0 and 1 representing the gait cycle.
        leg_index: 0 for FR, 1 for FL, 2 for BR, 3 for BL.
        Returns: 3D position of the foot.
        """
        # Apply phase offset for each leg
        phase = (phase + self.phase_offset[leg_index]) % 1.0

        # Swing phase
        if phase < 0.5:
            # Parabolic trajectory for swing
            x = self.step_length * (2 * phase - 0.5)
            z = self.step_height * (1 - (4 * (phase - 0.25))**2)
        # Stance phase
        else:
            x = self.step_length * (1.5 - 2 * phase)
            z = 0

        return np.array([x, 0, z])
