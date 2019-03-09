from django.urls import path

from .views import (
    HomeView,
    ImageIdentification
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('image/', ImageIdentification.as_view(), name='image_classifier'),
]
