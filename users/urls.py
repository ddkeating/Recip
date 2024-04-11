from django.urls import path
from .views import signup, LogInView, LogOutView

urlpatterns = [
    path('register/', signup, name='register'),
    # path('profile/', views.profile, name='profile'),
    path("login/", LogInView.as_view(), name='login'),
    path("logout/", LogOutView.as_view(), name='logout'),
]