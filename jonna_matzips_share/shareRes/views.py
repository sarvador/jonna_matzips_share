from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def index(request):
    #return HttpResponse("index")
    return render(request, 'shareRes/index.html')
def restaurantDetail(requset):
    #return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')
    
def restaurantCreate(requset):
    #return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')
    
def categoryCreate(requset):
    #return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')
