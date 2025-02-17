from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'value':3.14568468
    }
    return render(request, 'index.html',context)

def contact(request):
    return render(request, 'contact.html')

def dynamic_routing(request, number):
    return HttpResponse('you are in dynamic page')

def about(request):
    return render(request, 'about.html')