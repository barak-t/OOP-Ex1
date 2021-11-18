"""
Module for Simulation class.
"""
import Call
import Building
import Elevator

TIME_AFTER_LAST_CALL = 120
TIME_STEPS = 0.2

class ParametersError(Exception):
    pass

class Simulation(object):
    """
    Class for simulation the offline elevator algorithm.
    """
    def __init__(self, building_json, calls_csv):
        self.building = Building.Building(building_json)
        self.calls = Call.Call.load_calls_csv(calls_csv)
        # gets the total time of the simulation (lattes call + after time simulator)
        self.total_time = max(c.time for c in self.calls) + TIME_AFTER_LAST_CALL

        # Check if the calls and the building can run together.
        all_floors = sum([[c.source_f, c.dest_f] for c in self.calls], [])
        if min(all_floors) < self.building.min_floor or max(all_floors) > self.building.max_floor:
            raise ParametersError("Building and Calls files does not match. Calls min or max floor out of range.")

    def run(self):
        t = 0
        while(t < self.total_time):
            for e in self.building.elevators:
                e.update_calls()
                e.update_curr_pos(t)
                e.update_status()

            # Allocate an elevator for each calls that not allocate to elevator and its time relevant.
            calls_to_handle = self.not_allocate_calls(t)

            for c in calls_to_handle:
                self.allocate_elevator(c)

            t += TIME_STEPS

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
            elevs = [e for e in self.building.elevators if (
                       (e.its_up() and call.source_f >= e.curr_pos) or (e.its_down() and call.source_f <= e.curr_pos) or
                       e.its_level()) and
                       (e.min_f <= call.source_f <= e.max_f and e.min_f <= call.dest_f <= e.max_f)]

            if not elevs:
                return

            fastest_elev = min(elevs, key=lambda e:e.arrive_time(call.source_f))

        call.allocate_to = fastest_elev.id
        fastest_elev.add_call(call)  # Add this call to this elevator list

    def not_allocate_calls(self, t):
        """
        Returns the calls that not allocate to any elevator and relevant by time.
        """
        calls = []
        for c in self.calls:
            if c.time >= t:
                break
            if c.allocate_to == -1:
                calls.append(c)

        return calls

    def save(self, result_csv_path):
        """
        Saves the calls to csv file.
        Args:
            result_csv_path: the path to the output file.
        """
        Call.Call.save_calls_csv(result_csv_path, self.calls)

