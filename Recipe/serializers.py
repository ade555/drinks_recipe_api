from rest_framework import serializers
from . import models

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()
    class Meta:
        model = models.Recipe

        fields = '__all__'
    
    def get_ingredients(self, obj):
        return [ingredient.ingredient_name for ingredient in obj.ingredients.all()]