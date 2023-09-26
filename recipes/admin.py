from django.contrib import admin
from . models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(Category, CategoryAdmin)


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
