import json
import Elevator


class Building(object):
    max_floor = 0
    min_floor = 0
    elevators = []

    def __init__(self, json_file):
        with open(json_file) as f:
            j = json.load(f)

        self.min_floor = j["_minFloor"]
        self.max_floor = j["_maxFloor"]

        for elevator in j["_elevators"]:
            self.elevators.append(Elevator.Elevator(elevator['_id'], elevator['_speed'], elevator['_minFloor'],
                                                    elevator['_maxFloor'], elevator['_closeTime'],
                                                    elevator['_openTime'], elevator['_startTime'],
                                                    elevator['_stopTime']))
