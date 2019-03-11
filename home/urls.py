from django.urls import path

from .views import (
    HomeView,
    ImageIdentification,
    ObjectDetectionTest,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('image/', ImageIdentification.as_view(), name='image_classifier'),
    path('object-detection/', ObjectDetectionTest.as_view(), name='object_detection'),

]
