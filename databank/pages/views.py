from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'pages/home.html', context) 

def notes(request):
    context = {}
    return render(request, 'pages/notes.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def cs(request):
    context = {}
    return render(request, 'pages/cs.html', context)

def history(request):
    context = {}
    return render(request, 'pages/history.html', context)

def politics(request):
    context = {}
    return render(request, 'pages/politics.html', context)

def philosophy(request):
    context = {}
    return render(request, 'pages/philosophy.html', context)