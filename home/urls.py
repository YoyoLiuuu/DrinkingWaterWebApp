# added manuelly 
# map view functions 

from django.urls import path 
from . import home_views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#URLConf module 
urlpatterns = [
    path('', home_views.welcome),
    path('hello/', home_views.say_hello), #just passing to this function, not passing anything yet
]

urlpatterns += staticfiles_urlpatterns()