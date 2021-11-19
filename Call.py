"""
Module for Call class.
"""
import csv


class Call(object):
    """
    Represents a Call
    """

    def __init__(self, s, time, source_f, dest_f, f):
        self.time = float(time)
        self.source_f = int(source_f)
        self.dest_f = int(dest_f)
        self.s = s
        self.flag = f
        self.allocate_to = -1

    def its_up(self):
        """
        Returns if the call if for moving up.
        """
        return self.dest_f > self.source_f

    def its_down(self):
        """
        Returns if the call if for moving down.
        """
        return not self.its_up()

    @staticmethod
    def load_calls_csv(csv_path):
        """
        Creates list with Calls from a CSV file.
        Args:
            csv_path: The path to the CSV file.

        Returns:
            List of Calls.
        """
        calls = []
        with open(csv_path) as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=["s", "time", "src", "dst", "flag", "elev"])
            for row in reader:
                calls.append(Call(row["s"], row["time"], row["src"], row["dst"], row["flag"]))

        return calls

    @staticmethod
    def save_calls_csv(csv_path, calls):
        """
        Creates a csv file from list of calls
        Args:
            csv_path: The path to the destination csv file.
            calls: List of Call objects.
        """
        with open(csv_path, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            for c in calls:
                writer.writerow([c.s, c.time, c.source_f, c.dest_f, c.flag, c.allocate_to])

    def __repr__(self):
        return "<Call(time={t}, src={s}, dst={d})>".format(t=self.time, s=self.source_f, d=self.dest_f)
