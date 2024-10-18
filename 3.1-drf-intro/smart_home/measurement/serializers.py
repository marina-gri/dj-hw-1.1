from dataclasses import fields
from rest_framework import serializers
from django.forms import fields, ImageField

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']



class MeasurementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, max_length=None)
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']


    #cписок измерений
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']



