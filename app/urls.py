from django.urls import path, include
from .views import form, results, places, test

urlpatterns = [
    path('results', results),
    path('', form),
    path('places', places),
    path('test', test)
]
