from django.urls import path, include
from .views import form, places

urlpatterns = [
    path('', form),
    path('places', places)
]
