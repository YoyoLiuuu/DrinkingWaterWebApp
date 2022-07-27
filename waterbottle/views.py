from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def waterbottle(request):
    # Pull data from database 
    # Transform data
    # send email
    # etc 

    bottle = 2
    
    return render(request, 'bottle.html', {"waterbottle": bottle})

def notifications(request):
    return render(request, 'notifications.html')