from django.shortcuts import render
from .models import FoodItems
from datetime import date

# Create your views here.
def index(request) :
    return render(request, 'index.html')

