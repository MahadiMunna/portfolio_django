from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
# Create your views here.

def home(request):
    return render(request,'home.html') 
def about(request):
    return render(request,'about.html') 
def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contacts = contact()
        contacts.name = name
        contacts.email = email
        contacts.message = message
        contacts.save()
        return HttpResponse('<h1>Thanks for contact with us!!</h1>')
    return render(request,'contact.html') 
