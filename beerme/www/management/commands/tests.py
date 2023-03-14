from django.test import TestCase

# from django.db import models
# from django.contrib.auth.models import User
# import datetime as dt
# from django.utils import timezone


import unittest

# from django.contrib.auth.models import User
# from beerme.www.models import Race
import os

from django import setup
from django.conf import settings
from django.contrib.auth.models import User
from ...models import WeeklyBets, Bet, Tv, Track, Person, Team, Driver, Race

# Create your tests here.

# DJANGO_SETTING_MODULE = settings.configure()
# settings.configure()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beerme.settings")
setup()


class BetTest(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = "booboo"
        self.user.save()

        self.tv = Tv()
        self.tv.name = "BOOBTV"
        self.tv.save()

        self.track = Track()
        self.track.name = "Curtiss Speedway"
        self.track.save()

        self.team = Team()
        self.team.name = "Curtiss Racing"
        self.team.save()

        for p in ["Greg", "Bob"]:
            person = Person()
            person.name = p
            person.save()

        Driver.objects.create(name="Fast Bob", team_id=self.team)
        Driver.objects.create(name="Slow Greg", team_id=self.team)

    def test(self):
        self.assertTrue(True)

    def test_week(self):
        # w = WeeklyBets(3)
        # x = Bet()
        # x.user = 1
        # x.beer = True
        # x.save()
        oneBet = Bet.objects.all()
        # print(f"db={oneBet.count()}")
        self.assertTrue(oneBet.count() == 0)

    def test_tv(self):
        self.assertEqual(self.tv.name, "BOOBTV")

    def test_track(self):
        self.assertEqual(self.track.name, "Curtiss Speedway")

    def test_persons(self):
        self.assertEqual(Person.objects.all().count(), 2)

    def test_drivers(self):
        self.assertEqual(Driver.objects.all().count(), 2)

    def test_greg(self):
        self.assertEqual(Driver.objects.filter(name="Slow Greg").count(), 1)

    def test_bet(self):
        slow = Driver.objects.create(name="Slow Driver", team_id=self.team)
        fast = Driver.objects.create(name="Fast Driver", team_id=self.team)
        greg = Person.objects.create(name="Greg")
        bob = Person.objects.create(name="Bob")
        race = Race.objects.create(
            track_id=self.track, race_date="2003-03-03", tv_id=self.tv
        )
        bet_greg = Bet.objects.create(
            race_id=race, driver_id=slow, person_id=greg, finish=10
        )
        bet_bob = Bet.objects.create(
            race_id=race, driver_id=fast, person_id=bob, finish=3
        )
        bets = Bet.objects.all()
        week = WeeklyBets(race)
        self.assertEqual(week.pick_the_winner().person_id.name, "Bob")


# if __name__ == "__main__":
#     unittest.main()
