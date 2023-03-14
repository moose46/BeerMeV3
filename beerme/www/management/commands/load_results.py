from django.core.management.base import BaseCommand, CommandError
from www.models import Result, Race, Driver
from datetime import datetime
from ._read_results import read_results
from django.contrib.auth.models import User


# https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("race_date", nargs="+", type=str)

    def handle(self, *args, **options):
        try:
            print(f'{options["race_date"]}')

            race_date = datetime.date(
                datetime.strptime(options["race_date"][0], "%m/%d/%Y")
            )
            print(f"{race_date}")
            the_race = Race.objects.get(race_date=race_date)
            print(f"{the_race.track_id}")

        except Exception as e:
            print(f"{e}")
        loader = read_results(race_date=race_date)
        for x in loader:
            # print(f"{x.DRIVER}")
            try:
                # print(f"existing ... {x.DRIVER}")
                driver = Driver.objects.get(name=x.DRIVER)
                # continue
            except Exception as e:
                print(f"42 = {x.DRIVER} -> {e}")

                try:
                    # print(f"creating ... {x.DRIVER}")
                    user = User.objects.get(username="admin")
                    driver = Driver()
                    driver.name = x.DRIVER

                    driver.user_id = user.id
                    # driver.name = x.DRIVER
                    driver.save()
                except Exception as e:
                    print(e)
                    exit()

            try:
                # print(f"Creating {the_race} {x.DRIVER}")
                result = Result()
                result.driver_id_id = Driver.objects.get(name=x.DRIVER).pk
                result.race_id = the_race
                result.finished = x.POS
                result.save()
            except Exception as e:
                pass
                # print(e)
                # exit()

        results = Result.objects.all()
        print(f"# of results = {results.count()}")
