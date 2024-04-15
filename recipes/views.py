from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy  
from .models import Recipe
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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

    def get_queryset(self):
        category_name = self.kwargs.get('category_name', None)
        if category_name:
            return Recipe.objects.filter(category=category_name)
        else:
            return Recipe.objects.all()
        


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'


class HomeView(TemplateView):
    template_name = 'recipes/home.html'

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