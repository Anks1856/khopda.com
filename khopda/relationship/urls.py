from django.urls import path
from .import views

urlpatterns = [

    path('love/',views.love, name="love"),
    path('crush/', views.crush, name="crush"),
    path('mom/', views.mom, name="mom"),
    path('dad/', views.dad, name="dad"),
    path('bro/', views.bro, name="bro"),
    path('bestfrd/', views.bestfrd, name="bestfrd"),
    path('relative/', views.relative, name="relative"),
    path('hatter/', views.hatter, name="hatter"),
    path('teacher/', views.teacher, name="teacher"),
    path('rol/', views.rol, name="rol"),
    path('sup/', views.sup, name="sup"),
    path('clg/', views.clg, name="clg"),

    path('<int:post_id>', views.detail, name="detail"),
]