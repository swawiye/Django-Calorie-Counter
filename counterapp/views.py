from django.shortcuts import render
from .models import FoodItems
from datetime import date

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def food_list(request):
    return render(request, 'list_ops.html')