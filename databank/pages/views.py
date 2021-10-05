from django.shortcuts import render
from django.views import generic

from .models import NotePost

class NotePostList(generic.ListView):
    queryset = NotePost.objects.filter(status=1).order_by('-created_on')
    template_name = "notes.html"

class NotePostDetail(generic.DetailView):
    model = NotePost
    template_name = "notepost_detail.html"

def home(request):
    context = {}
    return render(request, 'pages/home.html', context) 

def notes(request):
    context = {}
    return render(request, 'pages/notes.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

