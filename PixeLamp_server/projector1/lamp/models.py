from django.db import models
from django.utils import timezone

class Rotations(models.Model):
    corner = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

class Bright(models.Model):
    bright = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

class On_Off(models.Model):
    on_off = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

class Up_down(models.Model):
    up_down = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)