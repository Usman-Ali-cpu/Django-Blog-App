from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import ArticleForm
from .models import Article
# Create your views here.


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        object = form.save()
        context['form'] = ArticleForm()
        context['object'] = object
        context['created'] = True
    return render(request, "articles/create.html", 
    context=context)


def article_search_view(request):
    context = {}
    if request.method == "GET":
        query = request.GET.get('query')
        qs = Article.objects.get(id=query)
        context = {
            'object': qs
        }
    return render(request, "articles/search.html", 
    context=context)
    

def article_detail_view(request, id=None):
    """
    it takes request as input and returns the HTML as a response
    """
    if id is not None:
        article_obj = Article.objects.get(id=id)
        if article_obj is None:
            return render(request, "articles/404.html", {})
        context = {
            'object': article_obj
        }
        
        return render(request, "articles/detail.html", context=context)
    else:
        return render(request, "articles/404.html", {})