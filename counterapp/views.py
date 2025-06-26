from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from datetime import date
from django.views.decorators.http import require_POST # for the form submission operations

# Create your views here.
def index(request):
    if request.method == "POST":
        food_item = request.POST['fooditem']
        calories = int(request.POST['calories'])
        FoodItem.objects.create(food_item=food_item, calories=calories)
        return redirect('food_list')
    return render(request, 'index.html')

def food_list(request):
    food_items = FoodItem.objects.filter(date_added=date.today())
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'list_ops.html', {
        'food_items': food_items,
        'total_calories': total_calories
    })

@require_POST
def delete_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    return redirect('food_list')

@require_POST
def reset_calories(request):
    FoodItem.objects.filter(date_added=date.today()).delete()
    return redirect('food_list')
