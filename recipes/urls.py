from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="home"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipes/create/', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name='about'),
]