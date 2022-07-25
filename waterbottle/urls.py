from django.urls import path 
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#URLConf module 
urlpatterns = [
    path('bottle/', views.waterbottle) #just passing to this function, not passing anything yet
]

urlpatterns += staticfiles_urlpatterns()