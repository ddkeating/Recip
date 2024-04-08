from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username}, your account has been created, please login!")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()  # Initialize form outside the 'POST' request block
    return render(request, 'users/register.html', {'form': form})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return redirect(reverse_lazy('user-login'))
        return super().dispatch(request, *args, **kwargs)

@login_required()    
def profile(request):
    return render(request, 'users/profile.html')