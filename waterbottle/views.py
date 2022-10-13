from django.shortcuts import render
from django.http import HttpResponse
from hello import hello_views
import pyrebase
from datetime import datetime
import json
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

# Create your views here.
def waterbottle(request):
    # Pull data from database 
    db = firebase.database()
    uid = hello_views.pass_id()
    user = db.child(uid).get()
    user_info = dict(user.val())
    
    # Transform data and get water cups today

    trackDict = json.dumps(user_info.get("tracking"))
    cups = user_info.get('water cups') 
    # send email
    # etc 

    
    return render(request, 'bottle.html', {"waterbottle": cups, "tracking": trackDict})

def notifications(request):
    db = firebase.database()
    uid = hello_views.pass_id()
    user = db.child(uid).get()
    user_info = dict(user.val())
    cups = user_info.get('water cups') 

    return render(request, 'notifications.html', {"cups": cups})


def waterGoal(request):
    if request.method == 'POST':
        db = firebase.database()
        uid = hello_views.pass_id()
    
        # GET THE INPUT VARIABLE
        numb_cups = request.POST.get('waterCups')
    
        # UPDATE WATER CUPS INFO IN THE DATABASE
        db.child(uid).update({"water cups": numb_cups})
        return render(request, 'notifications.html', {"cups": numb_cups})