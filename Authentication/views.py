from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from .form import CustomUserCreationForm, CustomLoginForm
from django.urls import reverse_lazy



class RegisterView(CreateView):
    
    template_name = 'register.html'
    form_class = CustomUserCreationForm  
    success_url = '/user/login/'  # Redirect to login page after successful registration

    
    
class UserLoginview(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/'
    
    
class UserLogoutiew(LogoutView):
    pass
     


def register(request):
    return HttpResponse("This is the register page.")