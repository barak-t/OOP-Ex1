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
        for t in range(self.total_time):
            for e in self.building.elevators:
                e.update_calls(t)
                e.update_curr_pos(t)

            # Allocate an elevator for each calls that not allocate to elevator and its time relevant.
            calls_to_handle = self.not_allocate_calls() 
            for c in calls_to_handle:
                self.allocate_elevator(c)
                if c.time > t:
                    break

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
            fastest_elev = self.building.elevators[0]

        else:
            # Gets the most fastest arrive elevator to this call
            fastest_elev = min((e for e in self.building.elevators),key=lambda e:e.arrive_time(call.source_f))

        call.allocate_to = fastest_elev.id
        fastest_elev.add_call(call)  # Add this call to this elevator list

    def not_allocate_calls(self):
        """
        Returns the calls that not allocate to any elevator sorted by time.
        """
        return sorted([c for c in self.calls if c.allocate_to == -1], key=lambda c: c.time)

