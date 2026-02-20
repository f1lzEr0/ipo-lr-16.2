from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name = "Главная"),
    path('shop', stationery, name = 'Концтовары'),
    path('about', info, name = 'О мне')
]