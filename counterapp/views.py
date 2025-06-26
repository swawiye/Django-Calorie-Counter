from django.shortcuts import render
from .models import FoodItems
from datetime import date

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def food_list(request):
    today = date.today()
    food_items = FoodItems.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'index.html', {'food_items': food_items, 'total_calories': total_calories})

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        FoodItems.objects.create(name=name, calories=calories)
    return render(request, 'index.html')

def delete_food(request, food_id):
    FoodItems.objects.get(id=food_id).delete()
    return render(request, 'index.html')

def reset_day(request):
    FoodItems.objects.filter(date_added=date.today()).delete()
    return render(request, 'index.html')
