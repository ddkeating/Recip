from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class LogOutView(LogoutView):
    template_name = 'registration/logout.html'
    def get_redirect_url(self):
        return reverse_lazy('logout')

class LogInView(LoginView):
    def get_redirect_url(self):
        return reverse_lazy('recipes-home')