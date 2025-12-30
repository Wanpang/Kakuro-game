from django.urls import path
from . import views

urlpatterns = [
    path('', views.kakuro_game, name='kakuro_game')
    
]