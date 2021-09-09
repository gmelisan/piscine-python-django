import random

from d06.settings import NAMES

class AnonuserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        name_exist = request.COOKIES.get('name')
        if name_exist:
            name = request.COOKIES['name']
        else:
            name = NAMES[random.randrange(len(NAMES))]
        request.anonname = name
            
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        if not name_exist:
            response.set_cookie('name', name, 42)

        return response
