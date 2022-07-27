from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response 
#request handler 
# action 

def get_live(username):
    no_water_days = 3 #change the code so we can get the specific days from database 

    if no_water_days == 0: 
        health = 'Super Healthy'
    elif no_water_days == 1:
        health = 'Drink more water to keep your flower healthy!'
    elif no_water_days == 2:
        health = 'Oh no your flower is dying. Please drink more water!'
    else:
        health = "You didn't drink enough water these days... your flower is dead... What if you can still save it?"

    return no_water_days+1, health

def say_hello(request):
    # Pull data from database 
    # Transform data
    # send email
    # etc 

    alive, health = get_live('myname')
    
    return render(request, 'flower.html', {'Health': health, 'alive': alive})

def welcome(request):
    return render(request, 'welcome.html')