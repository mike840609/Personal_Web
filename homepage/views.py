from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
 
    # return render(request,'blog/index.html')
     return render(request,'homepage/home.html')