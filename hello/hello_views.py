from distutils.command.config import config
import re
from urllib import request
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import admin
import pyrebase
import json
import requests
userID = ""

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


def send_notification(registration_ids, message_title, message_description):
    fcm_api="AAAAdB1eH4s:APA91bEI5pPOCWlPvk54fm6MmdbMgUEzVY6_0JLKezmU6qteUUQbjtNU2uE_39X_Qn8u_i33DNhQsD-qvUOuZ129caZqQ1UERO2wsYQxYTTdHoLCGbzgb0_b2TpyPBeNnFS5mF2ljMyG"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
        "Content-type":"application/json",
        "Authorization": 'key='+fcm_api
    }
    payload = {
        "registration_ids":registration_ids,
        "priority": "high",
        "notification": {
                "body": message_description,
                "title": message_title,
                "image": "https://us.123rf.com/450wm/yupiramos/yupiramos1803/yupiramos180307685/96803395-beautiful-flower-wink-cartoon-vector-illustration.jpg?ver=6",
                "icon": "https://img.freepik.com/premium-vector/cute-flower-cartoon-character_313669-38.jpg",
                "click_action": 'http://127.0.0.1:8000/home/hello/'
        }
       
    }
    result = requests.post(url, data=json.dumps(payload), headers=headers)

   

def send(request):
    registration =[]
    key = request.COOKIES.get('fcm_token')
    print(request.COOKIES)
    print(key)
    registration.append('eV4ORwwipTe9uDsA4KVtJX:APA91bHxqhcrZqLOi5CzLuCwHlThwqVjz3vq_GhTg3C2jhGBy9kIn5D-_VTPRnqC7Rf4V1pxl1zEQ7lTpw5k0GMRoFth7M3i8nKXVCU2Py4NW45xm3cqXF6Ok6hTTgBtpHn50wnVxHxT')
    # registration.append(key)
    send_notification(registration, "Reminder", "Drink more water to keep your flower healthy!")
    return HttpResponse("sent")

def showFirebaseJS(request):
   
    data=   'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
            'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js");' \
            'var firebaseConfig = {' \
                'apiKey: "AIzaSyB-fiT1Ju7Gf4dPdS9BbscZLnjvwycvtt4",'\
                'authDomain: "drink-water-database.firebaseapp.com",'\
                'databaseURL: "https://drink-water-database-default-rtdb.firebaseio.com",'\
                'projectId: "drink-water-database",'\
                'storageBucket: "drink-water-database.appspot.com",'\
                'messagingSenderId: "498708914059",'\
                'appId: "1:498708914059:web:32adf2844b31d65218598e",'\
                'measurementId: "G-TVZERVCL6F"'\
            '};'\
            'firebase.initializeApp(firebaseConfig);'\
            'const messaging = firebase.messaging();'\
            'messaging.setBackgroundMessageHandler(function(payload) {'\
                'console.log("Received background message", payload);'\
                'const notification = JSON.parse(payload);'\
                'const notificationOptions = {'\
                    'body: notification.body,'\
                    'icon: notification.icon,'\
                '};'\
                'return self.registration.showNotification(payload.notification.title, notificationOptions);'\
            '});'
           
            
    return HttpResponse(data, content_type="text/javascript")
def signIn(request):
    return render(request,"hello/home.html")

def home(request):
    return render(request,"hello/postsignin.html")
 
def postsignIn(request):
    global userID

    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!! Please check your information"
        return render(request,"hello/home.html",{"message":message})

    userID = user['localId']

    session_id=user['idToken']
    request.session['uid']=str(session_id)
    health, alive = get_live(email) #need to modify 
    return redirect('../home/hello', {'Health': health, 'alive': alive})#, {"email":email})#render(request,"",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"hello/home.html")
 
def signUp(request):
    return render(request,"hello/about.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']

        db = firebase.database()
        data = {"Email": email,
                "Checkboxes": "0",
                "Wake up": "00:00",
                "Bedtime": "00:00",
                "water cups": "0",
                "Remind hours": "0"
                }
        db.child(uid).set(data)

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

def pass_id():
    return userID