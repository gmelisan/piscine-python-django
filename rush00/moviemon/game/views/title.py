from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from game.engine.game import Game
from game.engine.statemanager import StateManager

class Title(TemplateView):
    template_name = "title.html"
    
    def get(self, request):
        sm = StateManager()
        key = request.GET.get('key')
        if key == 'a':
            game = Game()
            game.load_default_settings()
            sm.save(game.dump())
            return redirect('worldmap')
        if key == 'b':
            #return redirect('load')
            pass
            
        return render(request, self.template_name, {})
    
