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


class Tv(models.Model):
    name = models.CharField(max_length=24, default="FOX", null=True)

    def __str__(self) -> str:
        return self.name


class Race(base):
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE, default=-1)
    race_date = models.DateField(default=dt.date.today, unique=True)
    tv_id = models.ForeignKey(Tv, on_delete=models.CASCADE, null=True)
    tv = models.CharField(max_length=32, default="FOX")

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
    bet_str = f"{race_id}"

    def __str__(self) -> str:
        if self.beer:
            award = " --- BEER"
        else:
            award = ""
        return f"{self.person_id} - {self.race_id} - {self.driver_id} Finshed={self.finish} {award} {self.bet_str}"

    class Meta:
        ordering = ["race_id", "person_id"]
