from django.shortcuts import render
from movie.models import Actor, Genre,Movie


def home(reguests):
    actor =Actor.objects.all()
    ganre =Genre.objects.all()
    movie =Movie.objects.all()

    context = {
        'actor': actor,
        'ganre': ganre,
        'movie': movie
    }

    return render(reguests, 'index.html',context )

