"""
Module for Elevator class.
"""
from enum import Enum
import Call


class Status(Enum):
    MOVING_DOWN = -1
    LEVEL = 0
    MOVING_UP = 1


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
        self._status = Status.LEVEL
        self._last_time_moved = 0
        self.curr_pos = 0
        self.in_progress_calls = []
        self.delay = 0

    def its_up(self):
        return self.status == Status.MOVING_UP

    def its_down(self):
        return self.status == Status.MOVING_DOWN

    def its_level(self):
        return self.status == Status.LEVEL

    def arrive_time(self, dest_floor, way_stops=0):
        """
        Return the arrive time to a floor base on the current position of the elevator.
        Args:
            dest_floor: the destination floor of the elevator
            way_stops: how many times we need to stop

        Returns: the time its takes to arrive

        """

        is_up = True if dest_floor > self.curr_pos else False

        on_the_way = []

        for c in self.in_progress_calls:
            if c.its_up() and is_up:
                if c.status == Call.Status.GOING_TO_SRC and dest_floor > c.source_f > self.curr_pos:
                    on_the_way.append(c.source_f)
                elif c.status == Call.Status.GOING_TO_DEST and dest_floor > c.dest_f > self.curr_pos:
                    on_the_way.append(c.dest_f)
            elif c.its_down() and not is_up:
                if c.status == Call.Status.GOING_TO_SRC and dest_floor < c.source_f < self.curr_pos:
                    on_the_way.append(c.source_f)
                elif c.status == Call.Status.GOING_TO_DEST and dest_floor < c.dest_f < self.curr_pos:
                    on_the_way.append(c.dest_f)

        way_stops = len(set(on_the_way))

        return abs(dest_floor - self.curr_pos) / self.speed + \
               (self.stop_t + self.open_t + self.close_t + self.start_t) * (way_stops + 1)

    def add_call(self, call):
        """
        Add a call to the elevator.
        Args:
            call: the call to add
        """
        self.in_progress_calls.append(call)

    def update_calls(self):
        """
        Removes the already done calls from the calls list.
        """
        for call in self.in_progress_calls:
            if call.status == Call.Status.DONE:
                self.in_progress_calls.remove(call)

    def update_curr_pos(self, current_time):
        """
        Change the current position of the elevator base on the calls the elevator run.
        Args:
            current_time:
        """
        if self.status == Status.LEVEL:
            self.delay = self.close_t + self.start_t

        elif self._last_time_moved + 1/self.speed + self.delay <= current_time:
            self.delay = 0
            if self.status == Status.MOVING_UP:
                self.curr_pos += 1
                to_dst_up_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_DEST and c.its_up()]
                for c in to_dst_up_calls:
                    if c.dest_f == self.curr_pos:
                        c.status = Call.Status.DONE
                        self.delay = self.stop_t + self.open_t + self.close_t + self.start_t

                to_src_up_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_SRC and c.source_f == self.curr_pos]
                for c in to_src_up_calls:
                    c.status = Call.Status.GOING_TO_DEST
                    self.delay = self.stop_t + self.open_t + self.close_t + self.start_t

            elif self.status == Status.MOVING_DOWN:
                self.curr_pos -= 1
                to_dst_down_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_DEST and c.its_down()]
                for c in to_dst_down_calls:
                    if c.dest_f == self.curr_pos:
                        c.status = Call.Status.DONE
                        self.delay = self.stop_t + self.open_t + self.close_t + self.start_t

                to_src_down_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_SRC and c.source_f == self.curr_pos]
                for c in to_src_down_calls:
                    c.status = Call.Status.GOING_TO_DEST
                    self.delay = self.stop_t + self.open_t + self.close_t + self.start_t


            self._last_time_moved = current_time

            print(f"{current_time}, elev:{self.id}, pos:{self.curr_pos}, status:{self.status}")

    @property
    def status(self):
        return self._status

    def update_status(self):
        """
        Returns the elevator status (Status.LEVE, Status.MOVING_UP, Status.MOVING_DOWN)
        """

        if not self.in_progress_calls:
            self._status = Status.LEVEL

        elif self._status == Status.LEVEL:
            init_calls = [c for c in self.in_progress_calls if c.status == Call.Status.INIT]
            if init_calls:
                closest_call = min(init_calls, key=lambda c: self.arrive_time(c.source_f))
                closest_call.status = Call.Status.GOING_TO_SRC
                self._status = Status.MOVING_UP if self.curr_pos < closest_call.source_f else Status.MOVING_DOWN

        elif self._status == Status.MOVING_UP:
            init_up_calls = [c for c in self.in_progress_calls if c.status == Call.Status.INIT and c.its_up() and c.source_f > self.curr_pos]
            for c in init_up_calls:
                c.status = Call.Status.GOING_TO_SRC

            # Check if there is no calls in this direction but have calls in list -> Change direction
            to_src_up_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_SRC and c.source_f > self.curr_pos]
            to_dst_up_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_DEST and c.dest_f > self.curr_pos]

            if (not to_dst_up_calls and not to_src_up_calls) and self.in_progress_calls:
                self._status = Status.MOVING_DOWN

        elif self._status == Status.MOVING_DOWN:
            init_down_calls = [c for c in self.in_progress_calls if c.status == Call.Status.INIT and c.its_down() and c.source_f < self.curr_pos]
            for c in init_down_calls:
                c.status = Call.Status.GOING_TO_SRC

            # Check if there is no calls in this direction but have calls in list -> Change direction
            to_src_down_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_SRC and c.source_f < self.curr_pos]
            to_dst_down_calls = [c for c in self.in_progress_calls if c.status == Call.Status.GOING_TO_DEST and c.dest_f < self.curr_pos]

            if (not to_dst_down_calls and not to_src_down_calls) and self.in_progress_calls:
                self._status = Status.MOVING_UP

        return self._status
