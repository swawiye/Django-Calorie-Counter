from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_ops/', views.food_list, name='food_list'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'), # matches urls like: '/delete/1/', '<int:pk>'- expects an integer value in that part of the URL and assigns it to the variable pk (stands for primary key of a database record).
    path('reset/', views.reset_calories, name='reset_calories'),
]
