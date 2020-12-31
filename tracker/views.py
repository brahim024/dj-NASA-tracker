from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
def tracker(request):
    url='https://api.nasa.gov/techtransfer/patent/?engine&api_key=DEMO_KEY'
    data=requests.get(url)
    return render(request,'projects.html',{'data':data})