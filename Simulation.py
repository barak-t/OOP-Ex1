"""
Module for Simulation class.
"""
import Call
import Building


class ParametersError(Exception):
    pass


class Simulation(object):
    """
    Class for simulation the offline elevator algorithm.
    """
    def __init__(self, building_json, calls_csv):
        self.building = Building.Building(building_json)
        self.calls = Call.Call.load_calls_csv(calls_csv)

        # Check if the calls and the building can run together.
        all_floors = sum([[c.source_f, c.dest_f] for c in self.calls], [])
        if min(all_floors) < self.building.min_floor or max(all_floors) > self.building.max_floor:
            raise ParametersError("Building and Calls files does not match. Calls min or max floor out of range.")

    def run(self):
        """
        The main function of the algorithm.
        Allocate an elevator to every call.
        """
        for c in self.calls:
            self.allocate_elevator(c)

    def allocate_elevator(self, call):
        """
        Finds the ultimate elevator for a call.
        Args:
            call: The call object to assign an elevator.
        """
        # if there is only one elevator, allocate it.
        if len(self.building.elevators) == 1:
            self.building.elevators[0].add_call(call)  # Add this call to the only exist elevator

        else:
            all_times = []

            # Go over all elevator and add to list tuple with the time arrive calculation and elevator. (time, elevator).
            for e in self.building.elevators:
                call_arrived_at = e.time + e.arrive_time(call)

                # Check the time arrived for the call according to last elevator time and position.
                if e.time >= call.time:
                    call_arrived_at = e.arrive_time(call) + e.time - call.time
                    all_times.append((call_arrived_at, e))

                # Check if the elevator is now in call source floor.
                elif e.curr_pos == call.source_f:
                    call_arrived_at = e.time + e.arrive_to(call.source_f, call.dest_f)
                    all_times.append((call_arrived_at, e))

                else:
                    all_times.append((call_arrived_at, e))

            best = min(all_times, key=lambda x: x[0])  # Get the elevator with the minimal arrive time.
            best[1].add_call(call, best[0])  # Add this call to this elevator list

    def save(self, result_csv_path):
        """
        Saves the calls to csv file.
        Args:
            result_csv_path: the path to the output file.
        """
        Call.Call.save_calls_csv(result_csv_path, self.calls)
