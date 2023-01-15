from django.contrib import admin
from django.urls import path
from . import models, views



urlpatterns = [
    path("", views.menus_index, name="menus_index"),
    path("home", views.menus_index, name="home"),
    path("<int:pk>/", views.menus_detail, name="detail"),

]
