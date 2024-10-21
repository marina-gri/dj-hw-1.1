from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from measurement.views import SensorUpdateView, SensorListCreateView, MeasurementsCreateViewSet, MeasurementsListViewSet

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementsCreateViewSet.as_view()),
    path('measurements_list/', MeasurementsListViewSet.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
