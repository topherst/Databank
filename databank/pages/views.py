from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'pages/home.html', context) 

def notes(request):
    context = {}
    return render(request, 'pages/notes.html', context)