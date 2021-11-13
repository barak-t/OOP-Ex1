import json
import Elevator

class Building(object):
    _max_floor=0
    _min_floor=0
    _elevators = []

    def __init__(self, json_file):
        j = json.loads(json_file)

        self._min_floor = j["_minFloor"]
        self._max_floor = j["_maxFloor"]

        for elevator in j["_elevators"]:
            self._elevators.append(Elevator.Elevator(elevator['_id'], ))




