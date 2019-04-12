from django.urls import path, include
from .views import form, results, places

urlpatterns = [
    path('results', results),
    path('', form),
    path('places', places)
]
