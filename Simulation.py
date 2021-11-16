"""
Module for Simulation class.
"""
import Call
import Building


class Simulation(object):
    """
    Class for simulation the offline elevator algorithm.
    """
    def __init__(self, building_json, calls_csv):
        self.building = Building.Building(building_json)
        self.calls = Call.Call.load_calls_csv(calls_csv)

    def run(self):
        for c in self.calls:
            self.allocate_elevator(c)

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
            self.building.elevators[0].inprogress_calls.append(call)  # Add this call to this elevator list
            return


