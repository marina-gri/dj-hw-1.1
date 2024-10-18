from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
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


class MeasurementsViewSet(ViewSet):
    # получение списка измерений
    def list(self, request):
        queryset = Sensor.objects.all()
        serializer = SensorDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    # добавление измерения
    def create(self, request):
        new_data = request.data

        queryset = Measurement.objects.create(
            sensor_id=new_data['sensor'],
            temperature=new_data['temperature'],
            image=new_data.get('image')
        )

        queryset.save()
        serializer = MeasurementSerializer(queryset)
        return Response(serializer.data)

