from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
    # Class for representing a recipe with included steps and rating
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    date_added = models.DateField()

class Steps(models.Model):
    # Class to hold the step by step instructions for the recipes
    step_id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey(Recipe, db_column="recipe_id", on_delete=models.CASCADE)
    step_number = models.IntegerField(
        validators=[
            MaxValueValidator(1)
        ]
    )

class Ingredients(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey(Recipe, db_column="recipe_id", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    measurement = models.CharField(max_length=200)
    