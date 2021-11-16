"""
Module for Simulation class.
"""
import Call
import Building

TIME_AFTER_LAST_CALL = 120

class Simulation(object):
    """
    Class for simulation the offline elevator algorithm.
    """
    def __init__(self, building_json, calls_csv):
        self.building = Building.Building(building_json)
        self.calls = Call.Call.load_calls_csv(calls_csv)
        # gets the total time of the simulation (lattes call + after time simulator)
        self.total_time = max(c.time for c in self.calls) + TIME_AFTER_LAST_CALL

    def run(self):
        # for c in self.calls:
        #     self.allocate_elevator(c)

        for t in range(self.total_time):
            for e in self.building.elevators:
                e.update_calls(t)
                e.update_curr_pos(t)

            # TODO: Check if the first call that not allocate to any elevators (not_allocate_calls) is relevant.


    def save(self, result_csv_path):
        """
        Saves the calls to csv file.
        Args:
            result_csv_path: the path to the output file.
        """
        Call.Call.save_calls_csv(result_csv_path, self.calls)

    def allocate_elevator(self, call):
        """
        Finds the ultimate elevator for a call.
        Args:
            call: The call object to assign an elevator.
        """
        # if there is only one elevator, allocate it.
        if len(self.building.elevators) == 1:
            call.allocate_to = self.building.elevators[0].id
            self.building.elevators[0].add_call(call)  # Add this call to this elevator list
            return

        # check the most fastest arrive elevator to the call
        # TODO: Implement.

    def not_allocate_calls(self):
        """
        Returns the calls that not allocate to any elevator sorted by time.
        """
        return sorted([c for c in self.calls if c.allocate_to == -1], key=lambda c: c.time)

