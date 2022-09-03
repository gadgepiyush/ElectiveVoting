from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def vote(request):
    context = {
        "electives": ["Pattern Recognition", "Cryptography", "Distributed Computing", "Image Processing", "Graph Theory"]
    }
    return render(request, 'vote.html', context)


def info(request):
    return render(request, 'about.html')

