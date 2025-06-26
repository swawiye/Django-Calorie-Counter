from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_ops/', views.food_list, name='food_list'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
]
