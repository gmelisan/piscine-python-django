from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views.generic import *
from django.contrib.auth.forms import *
from django.contrib.auth import *

class IndexView(FormView):
    template_name = 'index.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        print('form_valid')
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return JsonResponse({"username": username}, status=200)

    def form_invalid(self, form):
        print('form_invalid')
        errors = form.errors.as_json()
        print('errors:', errors)
        return JsonResponse({"errors": errors}, status=400)

def logout_view(request):
    print('logout_view')
    if request.method == "POST" and request.is_ajax():
        logout(request)
        return JsonResponse({}, status=200)
    return redirect('index')
