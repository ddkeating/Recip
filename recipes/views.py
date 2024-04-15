from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy  
from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q


# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, "recipes/home.html", context)

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

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description']
    success_url = reverse_lazy('recipes-home')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.success_url = reverse_lazy('recipes-home')
        return super().form_valid(form)
    
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy( 'recipes-home' )

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


def about(request):
    return render(request, "recipes/about.html", {'title':'Recip | About'})