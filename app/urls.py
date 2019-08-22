from django.urls import path, include
from .views import form, places, card

urlpatterns = [
    path('', form),
    path('card', card),
    path('places', places)
]
