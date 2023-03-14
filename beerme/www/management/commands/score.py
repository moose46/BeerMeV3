from django.core.management.base import BaseCommand, CommandError
from www.models import Result, Race, Driver, WeeklyBets, Bet
from datetime import datetime
from ._read_results import read_results
from django.contrib.auth.models import User

import datetime as dt


# https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument("race_date", nargs="+", type=str)

    def handle(self, *args, **options):
        print("You scored!")
        races = Race.objects.filter(race_date__lte=dt.datetime.now().date())
        for race in races:
            bets = Bet.objects.filter(race_id=race)
            print()
            print(f"============= {race}")
            flg = 0
            for bet in bets:
                if flg == 0:
                    oneResult = Result.objects.get(
                        race_id=bet.race_id, driver_id=bet.driver_id
                    )
                    oneBet = bet
                    print(
                        f"oneResult = {oneResult.race_id}\n{bet.person_id} - {oneResult.driver_id} {oneResult.finished}"
                    )
                    flg = 1
                else:
                    twoResult = Result.objects.get(
                        race_id=bet.race_id, driver_id=bet.driver_id
                    )
                    twoBet = bet
                    print(
                        f"twoResult = {twoResult.race_id}\n{bet.person_id} - {twoResult.driver_id} {twoResult.finished}"
                    )
                    flg = 2
                if flg == 2:
                    if oneResult.finished < twoResult.finished:
                        print(f"winner = {oneBet} {oneResult}")
                    else:
                        print(f"winner = {twoBet} {twoResult}")
