import os
from django import setup
from django.db import models

from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# Create your models here.


class base(models.Model):
    now = timezone.datetime
    createdAt = models.DateTimeField("date created", auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updatedAt = models.DateTimeField("date last updated", auto_now_add=True, null=True)

    class Meta:
        abstract = True


class Person(base):
    name = models.CharField(max_length=32, default="")

    def __str__(self) -> str:
        return self.name


class Track(base):
    name = models.CharField(max_length=32, default="", unique=True)
    web_site = models.URLField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name:<32}"


class Team(base):
    name = models.CharField(max_length=32, default="", unique=True)

    def __str__(self) -> str:
        return self.name


class Driver(base):
    name = models.CharField(max_length=32, default="", unique=True)
    team_id = models.ForeignKey(Team, models.CASCADE, default=-1)

    def __str__(self) -> str:
        return f"{self.name:32} - Team {self.team_id}"

    class Meta:
        ordering = ["name"]


class Tv(base):
    name = models.CharField(max_length=24, default="FOX", null=True, unique=True)

    def __str__(self) -> str:
        return self.name


class Race(base):
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE, default=-1)
    race_date = models.DateField(default=dt.date.today, unique=True)
    tv_id = models.ForeignKey(Tv, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.race_date} - {self.track_id} - {self.tv_id}"

    class Meta:
        ordering = ["race_date"]


class Bet(base):
    race_id = models.ForeignKey(Race, on_delete=models.CASCADE, default=-1)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, default=-1)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, default=-1)
    finish = models.IntegerField(default=-1)
    beer = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.beer:
            award = " --- BEER"
        else:
            award = ""
        return f"{self.person_id} - {self.race_id} - {self.driver_id} Finshed={self.finish} {award}"

    class Meta:
        ordering = ["race_id", "person_id"]


class WeeklyBets:
    def __init__(self, prace_id: str) -> None:
        self.race_date = prace_id
        self.oneBet = Bet.objects.filter(race_id=prace_id)
        # print(self.oneBet)

    def pick_the_winner(self):
        # winner = self.oneBet[0]
        for i in self.oneBet:
            x = i
            if self.oneBet[0].finish > self.oneBet[1].finish:
                winner = self.oneBet[1]
                winner.beer = True
            else:
                winner = self.oneBet[0]
                winner.beer = True
        # print(f"winner 1 = {winner}")
        return winner

    def __str__(self) -> str:
        return self.oneBet


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beerme.settings")

    WeeklyBets(3)
