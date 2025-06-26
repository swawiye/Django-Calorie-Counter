from django.shortcuts import render, redirect, get_object_or_404 # 'redirect' -sends the user to a diff url, 'get_object_or_404' -fetches an object from the db; if it doesn't exist, it automatically returns a 404 (Not Found) error.
from .models import FoodItem
from datetime import date
from django.views.decorators.http import require_POST # for the form submission operations; Used to restrict a view so that it only works when the HTTP method is POST. If someone tries to access the view with a GET (or PUT, DELETE request), 405 Method Not Allowed response will be returned if the operation isn't allowed.

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
