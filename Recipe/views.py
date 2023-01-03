from django.shortcuts import render
from rest_framework import generics, filters
from. import serializers, models



class ViewRecipe(generics.ListAPIView):
    permission_class = ()

    authentication_class = ()

    serializer_class = serializers.RecipeSerialiser

    filter_backends = (filters.SearchFilter,)

    search_fields = ('$category',)

    def get_queryset(self):
        return models.Recipe.objects.all()


class FavoriteRecipe(generics.ListAPIView):
    permission_class = ()

    authentication_class = ()

    serializer_class = serializers.RecipeSerialiser

    filter_backends = (filters.SearchFilter,)

    search_fields = ('$category',)

    def get_queryset(self):
        return models.Recipe.objects.filter(category=True)