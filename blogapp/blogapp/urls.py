"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, re_path
from .view import home_view
from articles.views import article_detail_view
from articles.views import article_search_view
from articles.views import article_create_view
from accounts.views import login_view, logout_view, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', article_search_view),
    path('articles/create', article_create_view),
    path('articles/<int:id>/', article_detail_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('', home_view),
    # add urls for articles app
]