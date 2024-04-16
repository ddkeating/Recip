from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeCreateSuccessView, RecipeUpdateView, RecipeDeleteView, HomeView, AboutView, get_random_recipe

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipes/', RecipeListView.as_view(), name="recipes_list"),
    path('recipes/', RecipeListView.as_view(), name="recipes_list_by_search"),
    path('recipes/<str:category_name>/', RecipeListView.as_view(), name="recipes_list_by_category"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe/random/', get_random_recipe, name="random_recipe"),
    path('recipes/create/create/', RecipeCreateView.as_view(), name="create_recipe"),
    path('recipes/create/success/', RecipeCreateSuccessView.as_view(), name="create_recipe_success"),
    path('about/', AboutView.as_view(), name='about'),
]
