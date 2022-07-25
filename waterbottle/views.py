from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def waterbottle(request):
    # Pull data from database 
    # Transform data
    # send email
    # etc 
    
    return render(request, 'bottle.html')