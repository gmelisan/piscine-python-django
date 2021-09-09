from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Movies

def populate(request):
    data = [
        {
            'episode_nb': 1,
            'title': 'The Phantom Menace',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '1999-05-19'
        },
        {
            'episode_nb': 2,
            'title': 'Attack of the Clones',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2002-05-16'
        },
        {
            'episode_nb': 3,
            'title': 'Revenge of the Sith',
            'director': 'George Lucas',
            'producer': 'Rick McCallum',
            'release_date': '2005-05-19'
        },
        {
            'episode_nb': 4,
            'title': 'A New Hope',
            'director': 'George Lucas',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1977-05-25'
        },
        {
            'episode_nb': 5,
            'title': 'The Empire Strikes Back',
            'director': 'Irvin Kershner',
            'producer': 'Gary Kurtz, Rick McCallum',
            'release_date': '1980-05-17'
        },
        {
            'episode_nb': 6,
            'title': 'Return of the Jedi',
            'director': 'Richard Marquand',
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum',
            'release_date': '1983-05-25'
        },
        {
            'episode_nb': 7,
            'title': 'The Force Awakens',
            'director': 'J. J. Abrams',
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk',
            'release_date': '2015-12-11'
        }
    ]
    msg = ''

    for entry in data:
        try:
            Movies.objects.create(
                episode_nb=entry['episode_nb'],
                title=entry['title'],
                director=entry['director'],
                producer=entry['producer'],
                release_date=entry['release_date'],
            )
            msg += 'OK<br>'
        except Exception as e:
            msg += str(e) + '<br>'
    
    return HttpResponse(msg)

def display(request):
    errmsg = 'No data available'
    try:
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Exception()
        return render(request, 'ex05/display.html', {'movies': movies})

    except Exception as e:
        pass
    return HttpResponse(errmsg)


def remove(request):
    errmsg = 'No data available'
    if request.method == 'GET':
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Exception('no movies')
            titles = []
            for movie in movies:
                titles.append(movie.title)
            return render(request, 'ex05/remove.html', {'titles': titles})
                
        except Exception as e:
            print(e)
            
    elif request.method == 'POST':
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Exception('no movies')
            todel = request.POST.get('remove')
            Movies.objects.get(title=todel).delete()
            return redirect('remove')
        except Exception as e:
            print(e)
    return HttpResponse(errmsg)
