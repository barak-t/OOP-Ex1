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
        self.calls = Call.Call.create_calls_csv(calls_csv)

    def run(self):
        pass

    def save(self, result_csv_path):
        """
        Saves the calls to csv file.
        Args:
            result_csv_path: the path to the output file.
        """
        pass

    def allocate_elevator(self, call):
        """
        Finds the ultimate elevator for a call.
        Args:
            call: The call object to assign an elevator.
        """
        pass
