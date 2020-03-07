from django.urls import path
from .import views

urlpatterns = [
    path('love/', views.love, name="lovep"),
    path('motivational/', views.motivational, name="motivationalp"),
    path('attitude/', views.attitude, name="attitudep"),
    path('life/', views.life, name="lifep"),
    path('friendship/', views.friendship, name="friendshipp"),
    path('gods/', views.gods, name="godsp"),
    path('mother/', views.mother, name="mother"),
    path('nature/', views.nature, name="nature"),
]