from django import forms
from django.forms import ModelForm
from .models import Recipe

# Create a recipe form for users to add recipes
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image', 'ingredients', 'instructions', 'category', 'total_cook_time')