
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register'),
    path('login/',views.UserLoginview.as_view(), name='login'),
    path('logout/',views.UserLogoutiew.as_view(), name='logout')
    
    
    
] 
