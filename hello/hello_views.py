from distutils.command.config import config
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import admin
import pyrebase
from home import home_views

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
 
def signIn(request):
    return render(request,"home.html")

def home(request):
    return render(request,"postsignin.html")
 
def postsignIn(request):
    db = firebase.database()
    data = {"TOPGUN": "Maverick"}
    db.child("users").child("Bob").set(data)
    
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!! Please check your information"
        return render(request,"hello/home.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    health, alive = get_live(email) #need to modify 
    return redirect('../home/hello', {'Health': health, 'alive': alive})#, {"email":email})#render(request,"",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"home.html")
 
def signUp(request):
    return render(request,"hello/about.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     
     print(email)
     
     db = firebase.database()
     data = {"Username": name}
     db.child("users").set(data)
     
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "hello/about.html")
     message="Your account has been successfully created, please try logging in."
     return render(request,"hello/home.html",{"message":message})

#Allow switching pages through the navbar
def home(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )