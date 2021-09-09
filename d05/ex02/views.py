from django.shortcuts import render
from django.http import HttpResponse

import psycopg2

# Create your views here.

def init(request):
    try:
        with psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                dbname='djangotraining',
                                user='djangouser',
                                password='secret') as conn:
            with conn.cursor() as cur:
                s = 'CREATE TABLE ex02_movies( '
                s += 'title VARCHAR(64) UNIQUE NOT NULL,'
                s += 'episode_nb INT PRIMARY KEY,'
                s += 'opening_crawl TEXT,'
                s += 'director VARCHAR(32) NOT NULL,'
                s += 'producer VARCHAR(128) NOT NULL,'
                s += 'release_date DATE NOT NULL);'
                cur.execute(s)
                conn.commit()

    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('OK')

def populate(request):
    message = ''
    try:
        with psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                dbname='djangotraining',
                                user='djangouser',
                                password='secret') as conn:
            with conn.cursor() as cur:
                command = 'INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) '
                command += 'VALUES (%s, %s, %s, %s, %s);'
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
                
                for entry in data:
                    try:
                        cur.execute(command, [
                            entry['episode_nb'],
                            entry['title'],
                            entry['director'],
                            entry['producer'],
                            entry['release_date'],
                        ])
                        message += 'OK<br>'
                    except Exception as e:
                        message += str(e) + '<br>'
                conn.commit()

    except Exception as e:
        message += str(e)
    return HttpResponse(message)

def display(request):
    errmsg = 'No data available'
    try:
        with psycopg2.connect(host='127.0.0.1',
                                port=5432,
                                dbname='djangotraining',
                                user='djangouser',
                                password='secret') as conn:
            with conn.cursor() as cur:
                command = 'SELECT * FROM ex02_movies;'
                cur.execute(command)
                movies = cur.fetchall()
                if len(movies) == 0:
                    raise Exception()
            return render(request, 'ex02/display.html', {'movies': movies})

    except Exception as e:
        pass
    return HttpResponse(errmsg)
