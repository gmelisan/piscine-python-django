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
                s = 'CREATE TABLE ex00_movies( '
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
