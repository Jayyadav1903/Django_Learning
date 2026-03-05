from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("Hello, World! Welcome to my Django application.")
    return render(request, 'websites/home.html')



def about(request):
    return render(request, 'websites/about.html')

def contact(request):
    return render(request, 'websites/contact.html') 

