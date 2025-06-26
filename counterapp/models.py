from django.db import models

# Create your models here.
class FoodItems(models.Model): # instance for a table
    name = models.CharField(max_length=255) 
    calories = models.PositiveIntegerField()
    date_added = models.DateField()
    
    def __str__(self):
        return self.name