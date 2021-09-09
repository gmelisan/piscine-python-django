from django.views.generic import TemplateView
from django.shortcuts import redirect, render

class Battle(TemplateView):
    template_name = 'battle.html'

    def get(self, request, moviemon_id, key=None):
        context = {}
        return render(request, self.template_name, context)
