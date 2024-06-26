from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, HomeView, AboutView, get_random_recipe, AuthorDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipes/', RecipeListView.as_view(), name="recipes_list"),
    path('recipes/', RecipeListView.as_view(), name="recipes_list_by_search"),
    path('recipes/<str:category_name>/', RecipeListView.as_view(), name="recipes_list_by_category"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('recipe/random/', get_random_recipe, name="random_recipe"),
    path('recipes/create/add/', RecipeCreateView.as_view(), name="recipes_create"),
    path('recipes/create/success/', RecipeCreateView.as_view(), name="create_recipe_success"),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name="recipe_update"),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name="recipe_delete"),
    path('about/', AboutView.as_view(), name='about'),
    path('profile/<int:pk>/', AuthorDetailView.as_view(), name='profile'),
]
