from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('myassets', views.myassets, name='myassets'),
    
]