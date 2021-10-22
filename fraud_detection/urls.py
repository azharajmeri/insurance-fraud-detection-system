from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('fraud_detection', views.fraud_detection),
    path('result', views.result),
]
