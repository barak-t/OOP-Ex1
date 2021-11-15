"""
Module for Elevator class.
"""


class Elevator(object):
    """
    Represents an elevator.
    """
    def __init__(self, id, speed, min_f, max_f, close_t, open_t, start_t, stop_t):
        self.id = id
        self.speed = speed
        self.min_f = min_f
        self.max_f = max_f
        self.close_t = close_t
        self.open_t = open_t
        self.start_t = start_t
        self.stop_t = stop_t
