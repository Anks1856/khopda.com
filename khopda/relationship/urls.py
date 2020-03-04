from django.urls import path
from .import views

urlpatterns = [
    path('', views.relation, name="relation"),
    path('<int:post_id>', views.detail, name="detail"),
]