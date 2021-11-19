import os
import subprocess
import Ex1
from Simulation import ParametersError

CALLS_FOLDER= os.path.join("Ex1_input", "Ex1_Calls")
BUILDINGS_FOLDER = os.path.join("Ex1_input", "Ex1_Buildings")

SIMULATOR_NAME = "Ex1_checker_V1.2_obf.jar"
IDS = "206835977,206524266"

RUN_COMMAND = "java -jar {jar} {IDS} {B} {csv} {log}"
TESTER_LOG = "Tester_out_{B}__{C}.log"

OUTPUT_FORMAT = "out_{b}_{c}.csv"


def main():
    calls_files = os.listdir(CALLS_FOLDER)
    buildings_files = os.listdir(BUILDINGS_FOLDER) #["B5.json"]#

    for b in buildings_files:
        b = os.path.join(BUILDINGS_FOLDER, b)
        for c in calls_files:
            c = os.path.join(CALLS_FOLDER, c)
            out = OUTPUT_FORMAT.format(b=os.path.splitext(os.path.basename(b))[0], c=os.path.splitext(os.path.basename(c))[0])
            try:
                print(f"Start running {b} and {c}")
                # Ex1.main(b, c, out)
                subprocess.Popen(f"python3 Ex1.py {b} {c} {out}")
            except ParametersError:
                print(f"Can't run {b} and {c}")
                continue
            log = TESTER_LOG.format(B=os.path.splitext(os.path.basename(b))[0], C=os.path.splitext(os.path.basename(c))[0])
            subprocess.Popen(RUN_COMMAND.format(jar=SIMULATOR_NAME, IDS=IDS, B=b, csv=out, log=log))
            # input()


if __name__ == "__main__":
    main()