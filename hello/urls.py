from django.urls import path
from hello import hello_views
from home import home_views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

urlpatterns = [
    path('send/', hello_views.send),
    path('firebase-messaging-sw.js', hello_views.showFirebaseJS, name="show_firebase_js"),
    path("", hello_views.home, name="home"),
    path("hello/<name>", hello_views.hello_there, name="hello_there"),
    path("about/", hello_views.about, name="about"),
    path('check/', home_views.checkboxes),
]