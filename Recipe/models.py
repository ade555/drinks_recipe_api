from django.db import models

class RecipeIngredients(models.Model):
    ingredient_name = models.CharField(max_length=70)

    def __str__(self):
        return self.ingredient_name

    def natural_key(self):
        return self.ingredient_name


class Recipe(models.Model):
    name = models.CharField(max_length=35)
    category = models.CharField(max_length=35)
    image = models.URLField()
    ingredients = models.ManyToManyField(RecipeIngredients)
    favourite = models.BooleanField(default=False)
    instructions = models.TextField()

    def __str__(self):
        return self.name
