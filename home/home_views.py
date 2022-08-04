from tabnanny import check
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import check_form
from hello import hello_views
import pyrebase

# Create your views here.
# request -> response 
#request handler 
# action 

config= {
    "apiKey": "AIzaSyB-fiT1Ju7Gf4dPdS9BbscZLnjvwycvtt4",
    "authDomain": "drink-water-database.firebaseapp.com",
    "databaseURL": "https://drink-water-database-default-rtdb.firebaseio.com",
    "projectId": "drink-water-database",
    "storageBucket": "drink-water-database.appspot.com",
    "messagingSenderId": "498708914059",
    "appId": "1:498708914059:web:32adf2844b31d65218598e",
    "measurementId": "G-TVZERVCL6F"
}

# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

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
        db = firebase.database()

        #check_cups = request.POST.get('checkbox1')
        #print("hellllllllllllllllo", check_cups)
        #form = check_form(request.POST)
        #water_cups = form.water_cups()
        #hello_views.store_data(water_cups)
        box = request.POST.getlist('box')
        for i in box:
            cups += 1
        print(box)
        alive, health = get_live('myname')

        uid = hello_views.pass_id()

        db.child(uid).update({"water cups": cups})

    return render(request, 'flower.html', {'Health': health, 'alive': alive})