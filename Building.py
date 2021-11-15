"""
Module for Building class.
"""
import json
from Elevator import Elevator


class Building(object):
    """
    Represents a Building.
    """
    max_floor = 0
    min_floor = 0
    elevators = []

    def __init__(self, json_file):
        """
        Creates a building object form JSON file.
        Args:
            json_file: The path to the JSON file.
        """
        with open(json_file) as f:
            j = json.load(f)

        self.min_floor = j["_minFloor"]
        self.max_floor = j["_maxFloor"]

        # Create an elevator obj for each elevator element from the JSON and add it to the building elevator list.
        for elevator in j["_elevators"]:
            self.elevators.append(Elevator(elevator['_id'], elevator['_speed'], elevator['_minFloor'],
                                           elevator['_maxFloor'], elevator['_closeTime'], elevator['_openTime'],
                                           elevator['_startTime'], elevator['_stopTime']))
