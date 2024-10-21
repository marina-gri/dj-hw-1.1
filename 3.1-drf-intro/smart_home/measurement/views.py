from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


# получение списка датчиков и создание нового датчика
class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# изменение датчика
class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# добавление измерения
class MeasurementsCreateViewSet(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# получение списка измерений
class MeasurementsListViewSet(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer