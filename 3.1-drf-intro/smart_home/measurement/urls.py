from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from measurement.views import SensorUpdateView, SensorListCreateView, MeasurementsViewSet


router = DefaultRouter()
router.register(r'measurements', MeasurementsViewSet, basename='measurements')


urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
