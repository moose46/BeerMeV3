import logging
import csv
import re
from collections import defaultdict
from collections import namedtuple
from operator import itemgetter
from pathlib import Path
from time import strptime

DATE_FORMAT = "%m-%d-%Y"
file_path = Path.home() / "beerme" / "www" / "managment" / "commands"
log_file = Path.home() / "beerme" / "files_log.txt"
if not file_path.exists():
    file_path = Path.cwd() / "www" / "management" / "commands"
    log_file = Path.cwd() / "files_log.txt"


logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


def read_results(race_date):
    raw_data = list()
    # print(file_path.glob)
    # for f in file_path.glob(f"{race_date}*.txt"):
    print(f"reading... {race_date}")
    # race_track = f.stem.split("_")[1]
    with open(Path(f"{file_path}/{race_date}.txt"), "r") as file:
        reader = csv.reader(file, delimiter="\t")
        # csv file must have header
        rawResult = namedtuple("rawResult", next(reader), rename=True)
        # print(f"rawresult = {rawResult}")
        # Result = namedtuple('Result', [*rawResult._fields, 'picked_by', 'race_date', 'race_track'])
        # print(race_date)
        for row in reader:
            # print(row)
            # result = rawResult(*row)  # unpack csv data row into the named tuple
            raw_data.append(rawResult(*row))
            # print(result)
        # for x in raw_data:
        # print(x.DRIVER)
        return raw_data
