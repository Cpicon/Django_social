"""View files"""
#Django
from django.http import HttpResponse
#utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting"""
    date = datetime.now().strftime('%-I%p %A, %B of %Y')
    return HttpResponse('Hello, World! {}'.format(str(date)))

def second_function(request, name, age):
    """ return a greeting"""
    if age<18:
        message = 'sorry'
    else:
        message = 'hi'
    return HttpResponse(message)