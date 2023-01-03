from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Recipe, RecipeIngredients
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    pass

admin.site.register(RecipeIngredients)
