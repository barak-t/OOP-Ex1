"""
The main module of the program
"""
import argparse
from Simulation import Simulation


def main(b_json, c_csv, out_csv):
    """
    The main function of the program.
    """
    # Run the simulation with the given args and save the output.
    s = Simulation(b_json, c_csv)
    s.run()
    s.save(out_csv)


if __name__ == '__main__':
    # Create parser for the required arguments.
    parser = argparse.ArgumentParser(description="Offline algorithm for assign calls for elevators.",
                                     usage="Ex1.py <Building.json> <Calls.csv> <output.csv>")
    parser.add_argument("building_json_file", help="The path to the JSON file of the building")
    parser.add_argument("calls_csv_file", help="The path to the CSV file of the calls")
    parser.add_argument("output_file", help="The path to the output CSV file")
    args = parser.parse_args()

    main(args.building_json_file, args.calls_csv_file, args.output_file)

