from django.urls import path
from .import views

urlpatterns = [
    path('relationships/', views.relation, name="relation"),
]