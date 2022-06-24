from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.Login, name='lgout'),
    path('logout', views.Logout),
    
]