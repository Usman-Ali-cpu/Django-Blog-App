"""
To render html Web Pages
"""

import random
from django.shortcuts import render
from django.http import HttpResponse





def home_view(request):
    """
    it takes request as input and returns the HTML as a response
    """
    name = "Osman"
    number = random.randint(0, 100000)
    HTML_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    return HttpResponse(HTML_STRING)