from django.urls import path
from .import views

urlpatterns = [
    path('poetries/', views.poetry, name="poetry"),
]