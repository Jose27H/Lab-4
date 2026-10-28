"""
Lab 2 line follower - complete solution, provided as a starting point for Lab 4.

Step 2 (Task 2): line_position()  - perception: 4 sensors -> one number
Step 3 (Task 3): LineFollower     - action: that number -> a velocity
"""
from turbopi.config import FOLLOW_SPEED, TURN_GAIN, SEARCH_TURN

# Where each sensor sits, left to right, in "sensor widths" from the centre.
SENSOR_WEIGHTS = (-1.5, -0.5, 0.5, 1.5)


def line_position(sensors):
    """sensors: 4 booleans (leftmost .. rightmost), True = sees black.
    Returns the average position of the sensors that see the line
    (negative = line is LEFT of centre), or None if none of them do."""
    seen = [w for w, s in zip(SENSOR_WEIGHTS, sensors) if s]
    if not seen:
        return None
    return sum(seen) / len(seen)


class LineFollower:
    """A model-based reflex agent: percept -> action, plus one piece of
    memory (where the line was last seen)."""

    def __init__(self):
        self.last_position = None           # Step 3B: memory; None = never seen

    def step(self, sensors):
        """Called 10 times a second. Returns (lx, ly, az)."""
        pos = line_position(sensors)
        if pos is None:                     # Step 3B: line lost
            if self.last_position is None or self.last_position == 0:
                return 0.0, 0.0, 0.0
            if self.last_position < 0:
                return 0.0, 0.0, SEARCH_TURN        # it went off to the LEFT
            return 0.0, 0.0, -SEARCH_TURN           # it went off to the RIGHT
        self.last_position = pos            # Step 3B: remember
        # Step 3A: line LEFT (pos < 0) -> turn LEFT (+az): hence the minus sign
        return FOLLOW_SPEED, 0.0, -TURN_GAIN * pos
