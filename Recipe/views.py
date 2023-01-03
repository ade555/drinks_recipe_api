from django.http import JsonResponse
from rest_framework import generics, filters
from. import serializers, models



class ViewRecipe(generics.ListAPIView):
    permission_class = ()

    authentication_class = ()

    queryset = models.Recipe.objects.all()

    serializer_class = serializers.RecipeSerializer

    filter_backends = (filters.SearchFilter,)

    search_fields = ('$category',)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse({'recipe': serializer.data})


class FavoriteRecipe(generics.ListAPIView):
    permission_class = ()

    authentication_class = ()

    serializer_class = serializers.RecipeSerializer

    filter_backends = (filters.SearchFilter,)

    search_fields = ('$category',)

    def get_queryset(self):
        return models.Recipe.objects.filter(category=True)