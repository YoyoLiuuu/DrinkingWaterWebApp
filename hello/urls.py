from django.urls import path
from hello import hello_views
from home import home_views

urlpatterns = [
    path("", hello_views.home, name="home"),
    path("hello/<name>", hello_views.hello_there, name="hello_there"),
    path("about/", hello_views.about, name="about"),
    path('check/', home_views.checkboxes)

]