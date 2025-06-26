from django.db import models

# Create your models here.
class FoodItem(models.Model): # instance for a table
    food_item = models.CharField(max_length=255) 
    calories = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True) # automatically sets the date added to the current date
    
    def __str__(self):
        return self.food_item