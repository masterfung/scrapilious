from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def listings(request):
    return render(request, 'listings.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def graphs(request):
    return render(request, 'graphs.html')


def login(request):
    return render(request, 'registration/login.html')