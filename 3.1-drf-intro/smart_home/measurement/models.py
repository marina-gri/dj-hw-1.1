from dataclasses import fields
from django.forms import fields

from django.db import models
from rest_framework.fields import ImageField


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField()


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, blank=False, related_name='measurements')
    temperature = models.CharField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


