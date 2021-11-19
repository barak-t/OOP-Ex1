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
        self.last_pos = 0
        self.curr_pos = 0
        self.last_time = 0
        self.time = 0
        self.delay = self.close_t + self.start_t + self.stop_t + self.open_t

    def its_up(self):
        """
        Returns if the elevator is going up.
        """
        return self.last_pos < self.curr_pos

    def arrive_time(self, call):
        """
        Return the arrive time to a dest floor of a call base on the current position of the elevator.
        Args:
            call: the call to calculate for.

        Returns: the time its takes to arrive
        """
        time_to_src = abs(self.curr_pos - call.source_f)/self.speed + self.delay
        time_src_dst = abs(call.source_f - call.dest_f)/self.speed + self.delay
        return time_to_src + time_src_dst

    def arrive_to(self, src, dest):
        """
        Calculate the time is take to move the elevator from src to dest floors
        Args:
            src: source floor
            dest: destination floor
        """
        return abs(src - dest) / self.speed + self.delay

    def add_call(self, call, t=0):
        """
        Add a call to the elevator.
        Args:
            call: the call to add.
            t: the time the elevator will get the the dest of the call.
        """
        call.allocate_to = self.id
        self.last_pos = self.curr_pos
        self.curr_pos = call.dest_f

        self.last_time = self.time
        self.time = call.time + t
