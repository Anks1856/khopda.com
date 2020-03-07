from django.urls import path
from .import views

urlpatterns = [
    path('love/', views.love, name="loveq"),
    path('motivation/', views.motivation, name="motivation"),
    path('attitude/', views.attitude, name="attitude"),
    path('life/', views.life, name="life"),
    path('friendship/', views.friendship, name="friendship"),
    path('god/', views.god, name="god"),
]


