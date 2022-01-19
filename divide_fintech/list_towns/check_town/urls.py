from django.urls import path, include
from .views import findTown
urlpatterns = [
    path('', findTown),
]