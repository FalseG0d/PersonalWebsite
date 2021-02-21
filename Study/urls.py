from django.urls import path
from . import views
urlpatterns = [
    path('dates', views.date),
]
