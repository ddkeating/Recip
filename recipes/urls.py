from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipes/', RecipeListView.as_view(), name="recipes_list"),
    path('recipes/<str:search_query>/', RecipeListView.as_view(), name="recipes_list_by_search"),
    path('recipes/<str:category_name>/', RecipeListView.as_view(), name="recipes_list_by_category"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),

    # path('recipes/create/', RecipeCreateView.as_view(), name="recipes-create"),
    # path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name="recipes-update"),
    # path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', AboutView.as_view(), name='about'),
]
