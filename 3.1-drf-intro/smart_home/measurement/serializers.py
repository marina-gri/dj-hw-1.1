from dataclasses import fields
from rest_framework import serializers
from django.forms import fields, ImageField

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, max_length=None)
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']


class MeasurementDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, max_length=None)
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']


    #cписок измерений
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']



