from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def home(request):
    # return HttpResponse('<h1> Welcome to home page</h1>')
    search_term = request.GET.get('search_movie')     
    # movies = Movie.objects.all()

    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()
    
    return render(request, 'home.html', 
                  {'search_term': search_term, 'movies': movies})


def about(request):
    return HttpResponse('<h1> Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})