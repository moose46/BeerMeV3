import os
from django import setup
from django.db import models
import os
import sys
import django


# from django.contrib.auth.models import User

from django.contrib import admin

import logging
import csv
import re
from collections import defaultdict
from collections import namedtuple
from operator import itemgetter
from pathlib import Path
from time import strptime

DATE_FORMAT = "%m-%d-%Y"
file_path = Path.home() / "beerme" / "results"
log_file = Path.home() / "beerme" / "files_log.txt"
if not file_path.exists():
    file_path = Path.cwd() / "data"
    log_file = Path.cwd() / "files_log.txt"


# from beerme.www.models import Race

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)
DriverBet = namedtuple("DriverBet", "date, person_name, driver_name")


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(f"{BASE_DIR}")
    print(f"... {BASE_DIR} \n{__file__}\n {os.path.abspath(__file__)}")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beerme.settings")
    django.setup()
    from models import Race
