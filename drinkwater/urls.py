"""drinkwater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hello import hello_views
from home import home_views


urlpatterns = [
    path('', include("hello.urls")),
    
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('waterbottle/', include('waterbottle.urls')),
    path('login/', hello_views.signIn),
    path('postsignIn/', hello_views.postsignIn),
    path('signUp/', hello_views.signUp, name="signup"),
    path('logout/', hello_views.logout, name="log"),
    path('postsignUp/', hello_views.postsignUp),
    
]

urlpatterns += staticfiles_urlpatterns()