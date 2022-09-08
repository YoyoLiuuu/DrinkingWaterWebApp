from tabnanny import check
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from pyparsing import originalTextFor
from .forms import check_form
from hello import hello_views
import pyrebase
from django.contrib import messages
from datetime import datetime, timedelta

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

def get_live(username, no_water_days):
    # no_water_days = 2 #change the code so we can get the specific days from database 
   
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
    db = firebase.database()
    uid = hello_views.pass_id()
    user = db.child(uid).get()

    user_info = dict(user.val())

    cups = user_info.get('water cups')

    # Check if user drank enough water in last 2 days
    # TODAY
    count = 0
    d = datetime.today().date()
    today = user_info.get("tracking").get(str(d))
    if today == None or int(today) < 8:
        count = count + 1
    # One day ago
    d = (datetime.today() - timedelta(days=1)).date()
    oneDayAgo = user_info.get("tracking").get(str(d))
    if oneDayAgo == None or int(oneDayAgo) < 8:
        count = count+ 1
        
    # Two days ago
    d = (datetime.today() - timedelta(days=2)).date()
    twoDaysAgo = user_info.get("tracking").get(str(d))
    if twoDaysAgo == None or int(twoDaysAgo) < 8:
        count = count + 1     


    cups_decrease = False

    alive, health = get_live('myname', count)
    
    return render(request, 'flower.html', {'Health': health, 'alive': alive, 'cups': cups, 'cups_decrease': cups_decrease})

def welcome(request):
    alert = False
    return render(request, 'welcome.html', {'alert': alert})


def checkboxes(request):
    cups = 0
    cups_decrease = False
    if request.method == 'POST':
        db = firebase.database()

        box = request.POST.getlist('box')
        for i in box:
            cups += 1


        # Check if user drank enough water in last 2 days
        # alive, health = get_live('myname', 1)

        uid = hello_views.pass_id()

        #the next 3 lines of code needs to be tested before sure it works 
        if uid == "":
            alert = True 
            return render(request, 'welcome.html', {'alert': alert})

        user = db.child(uid).get()
        user_info = dict(user.val())

        original_cups = user_info.get('water cups')

        # if int(original_cups) <= int(cups):
        #     db.child(uid).update({"water cups": cups})
        #     return render(request, 'flower.html', {'Health': health, 'alive': alive, 'cups': cups, 'cups_decrease': cups_decrease})

        # else: 
        #     cups_decrease = True
        #     db.child(uid).update({"water cups": cups})
        #     return render(request, 'flower.html', {'Health': health, 'alive': alive, 'cups': original_cups, 'cups_decrease': cups_decrease})

        if int(original_cups) > int(cups): 
            cups_decrease = True

        # UPDATE INFO IN THE DATABASE
        db.child(uid).update({"water cups": cups})
        d = datetime.today().date()
        db.child(uid).child("tracking").child(d).set(cups)


        # CHECK IF USER DRANK ENOUGH WATER THESE 3 DAYS
        count = 0
        if cups < 8:
            count = count + 1
        # One day ago
        d = (datetime.today() - timedelta(days=1)).date()
        oneDayAgo = user_info.get("tracking").get(str(d))
        if oneDayAgo == None or int(oneDayAgo) < 8:
            count = count+ 1
            
        # Two days ago
        d = (datetime.today() - timedelta(days=2)).date()
        twoDaysAgo = user_info.get("tracking").get(str(d))
        if twoDaysAgo == None or int(twoDaysAgo) < 8:
            count = count + 1

        # SET alive, health
        alive, health = get_live('myname', count)

        return render(request, 'flower.html', {'Health': health, 'alive': alive, 'cups': cups, 'cups_decrease': cups_decrease})