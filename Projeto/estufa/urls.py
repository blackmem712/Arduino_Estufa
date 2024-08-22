from django.contrib import admin
from django.urls import path
from .views import estufa, get_latest_data, processa_form,dashboard



urlpatterns = [
    path('estufa/', estufa, name='estufa'),    
    path('processa_form/', processa_form, name="processa_form"),
    path('get-latest-data/', get_latest_data, name='get_latest_data'),
      path('estufa/dashboard/', dashboard, name="processa_form"),
]

