from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.text),
    path('tovari/', views.text2),
    path('otziv/', views.text3),
]
