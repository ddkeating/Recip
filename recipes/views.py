from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy  
from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from random import randint
from .forms import RecipeForm



def get_random_recipe(request):
    total_recipes = Recipe.objects.count()
    random_index = randint(0, total_recipes - 1)
    random_recipe = Recipe.objects.all()[random_index]
    return redirect('recipe_detail', pk=random_recipe.pk)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipe_list'

# This method is used to filter recipes by category or search.
    def get_queryset(self):
        category_name = self.kwargs.get('category_name', None)
        search_query = self.request.GET.get('search_query', '')
        if category_name:
            return Recipe.objects.filter(category=category_name)
        # Searches by passed query. If no query is passed, returns all recipes
        elif search_query:
            if (search_query == ''):
                return Recipe.objects.all() 
            return Recipe.objects.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        else:
            return Recipe.objects.all()
        


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'


class HomeView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipe_list'

class AboutView(TemplateView):
    template_name = 'recipes/about.html'

class RecipeCreateSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'recipes/create_recipe_success.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipes/create_recipe.html '
    form_class = RecipeForm
    success_url = reverse_lazy('create_recipe_success')

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Save the image file
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Recipe'
        return context
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    # fields = ['title', 'description', 'category', 'ingredients', 'instructions', 'image', 'total_cook_time']
    template_name = 'recipes/update_recipe.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        # Save the image file
        form.instance.image = self.request.FILES.get('image')
        return super().form_valid(form)
    
    def test_func(self):
            recipe = self.get_object()
            if self.request.user == recipe.author:
                return True
            return False

    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})
    
    def test_func(self):
            recipe = self.get_object()
            if self.request.user == recipe.author:
                return True
            return False

class AuthorDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        recipes = Recipe.objects.filter(author=user)
        context['recipes'] = recipes
        return context
    
    def test_func(self):
            user = self.get_object()
            if self.request.user == user:
                return True
            return False
    

