from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from game.engine.game import Game
from game.engine.statemanager import StateManager

class Worldmap(TemplateView):
    template_name = "worldmap.html"

    help_text = 'Arrows to move, start - option, select - moviedex'

    def __init__(self):
        pass
        
    def get(self, request):
        sm = StateManager()
        data = sm.load()
        if not data:
            return redirect('title')
        game = Game()
        game.load(data)
        key = request.GET.get('key')
        if key:
            if key == 'up':
                r = game.move(0, -1)
            if key == 'down':
                r = game.move(0, 1)
            if key == 'left':
                r = game.move(-1, 0)
            if key == 'right':
                r = game.move(1, 0)
            if r == True:
                print('------------ battle')
                return redirect('battle', moviemon_id=game.get_random_movie())
            if key == 'select':
                return redirect('moviedex')
            if key == 'start':
                return redirect('title')
           
            sm.save(game.dump())
            return redirect('worldmap')
        context = {
            'map': game.m,
            'movieballs': game.movieballs,
            'message': game.message
        }
        return render(request, self.template_name, context)
