from django.urls import path, include
from rest_framework.routers import DefaultRouter

from measurement.views import SensorUpdateView, SensorListCreateView, MeasurementsViewSet

router = DefaultRouter()
router.register(r'measurements', MeasurementsViewSet, basename='measurements')


urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('', include(router.urls)),
]
