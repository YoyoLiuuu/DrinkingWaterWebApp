from tabnanny import check
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import check_form
from hello import hello_views

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

def login(request):
    return render(request, "flower.html")

def checkboxes(request):
    cups = 0
    if request.method == 'POST':
        #check_cups = request.POST.get('checkbox1')
        #print("hellllllllllllllllo", check_cups)
        #form = check_form(request.POST)
        #water_cups = form.water_cups()
        #hello_views.store_data(water_cups)
        box = request.POST.getlist('box')
        for i in box:
            cups += 1
        alive, health = get_live('myname')
        hello_views.store_data(cups)
    return render(request, 'flower.html', {'Health': health, 'alive': alive})