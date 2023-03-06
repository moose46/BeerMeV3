from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=32)


class Track(models.Model):
    name = models.CharField(max_length=32)


class Driver(models.Model):
    name = models.CharField(max_length=32)


class Race(models.Model):
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE)
    race_date = models.DateField()


class Bet(models.Model):
    race_date = models.DateField()
    person_name = models.ForeignKey(Person, on_delete=models.CASCADE)
