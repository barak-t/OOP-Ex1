import Call
import Building


class Simulation(object):
    def __init__(self, building_json, calls_csv):
        self.building = Building.Building(building_json)
        self.calls = Call.Call.create_calls_csv(calls_csv)

    def run(self):
        pass

    def save(self, result_csv_path):
        pass

    def allocate_elevator(self, call):
        pass


def main():
    s = Simulation("", "")
    s.run()




if __name__ == '__main__':
    main()
