from django.urls import path, include
from .views import form, results

urlpatterns = [
    path('results', results, name="results"),
    path('', form.as_view()),
]
