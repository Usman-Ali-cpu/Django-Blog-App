"""
To render html Web Pages
"""

import random
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    it takes request as input and returns the HTML as a response
    """
    name = "Osman"
    print(args, kwargs)
    number = random.randint(0, 100000)
    article_obj = Article.objects.get(id=2)
    article_title = article_obj.title
    article_content = article_obj.content
    article_id = article_obj.id
    object_list = Article.objects.all()
    context = {
        "title": article_title,
        "id": article_id,
        "content": article_content,
        "obj_list": object_list,
    }
    
    
    
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)

