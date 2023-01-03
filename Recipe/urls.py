from django.urls import path
from . import views

urlpatterns = [
    path('recipe', views.ViewRecipe.as_view(), name='recipe'),
    path('favorites', views.FavoriteRecipe.as_view(), name='favorites'),
]