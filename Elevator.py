"""
Module for Elevator class.
"""
from enum import Enum


class Status(Enum):
    MOVING_DOWN = -1
    LEVEL = 0
    MOVING_UP = 1


class Elevator(object):
    """
    Represents an elevator.
    """

    curr_pos = 0
    in_progress_calls = []

    def __init__(self, id, speed, min_f, max_f, close_t, open_t, start_t, stop_t):
        self.id = id
        self.speed = speed
        self.min_f = min_f
        self.max_f = max_f
        self.close_t = close_t
        self.open_t = open_t
        self.start_t = start_t
        self.stop_t = stop_t

    def arrive_time(self, dest_floor):
        """
        Return the arrive time to a floor base on the current position of the elevator.
        Args:
            dest_floor:

        Returns:

        """
        # TODO: Implement.
        pass

    def add_call(self, call):
        """
        Add a call to the elevator.
        Args:
            call:
        """
        # TODO: Implement.
        pass

    def update_calls(self, current_time):
        """
        Removes the already done calls from the calls list.
        Args:
            current_time:
        """
        # TODO: Implement.
        pass

    def update_curr_pos(self, current_time):
        """
        Change the current position of the elevator base on the calls the elevator run.
        Args:
            current_time:
        """
        # TODO: Implement
        pass

    @property
    def status(self):
        """
        Returns the elevator status (Status.LEVE, Status.MOVING_UP, Status.MOVING_DOWN)
        """
        pass
        return Status.MOVING_UP