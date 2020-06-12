from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('' , include('login_site.urls')),
    path('login.html',include('login_site.urls')),
    path('signup.html',include('login_site.urls')),
    path('home.html' ,include('login_site.urls')),
    path('admin/', admin.site.urls),

]
