from django.views.generic import TemplateView
from django.shortcuts import redirect, render

class Moviedex(TemplateView):

    template_name = 'moviedex.html'

    def get(self, request):

        key = request.GET.get('key')
        if (key == 'select'):
            return redirect('worldmap')

        context = {}
        return render(request, self.template_name, context)
