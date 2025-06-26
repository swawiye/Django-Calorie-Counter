from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list_ops', views.food_list, name="food_list")
]