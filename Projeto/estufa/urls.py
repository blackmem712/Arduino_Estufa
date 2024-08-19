from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('estufa/', views.estufa, name='estufa'),    
    path('processa_form/',views.processa_form, name="processa_form"),
]

