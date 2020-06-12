from . import views
from django.urls import path

urlpatterns = [
    path('', views.home , name='home'),
    path('login.html',views.login ),
    path('signup.html',views.signup ),
    path('home.html',views.home ),
]