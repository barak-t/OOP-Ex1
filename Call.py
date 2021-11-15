import csv


class Call(object):

    allocate_to = -1

    def __init__(self, time, source_f, dest_f):
        self.time = float(time)
        self.source_f = int(source_f)
        self.dest_f = int(dest_f)

    def its_up(self):
        return self.dest_f > self.source_f

    def its_down(self):
        return not self.its_up()

    @staticmethod
    def create_calls_csv(csv_path):
        calls = []
        with open(csv_path) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["s", "time", "src", "dst", "flag", "elev"])
            for row in reader:
                calls.append(Call(row["time"], row["src"], row["dst"]))

        return calls

    def __repr__(self):
        return "<Call (time:{t} src:{s} dst:{d})>".format(t=self.time, s=self.source_f, d=self.dest_f)

