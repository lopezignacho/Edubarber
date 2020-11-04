from django.urls import path
from .views import home, registro, reservation

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('reservation/', reservation, name="reservation")
]