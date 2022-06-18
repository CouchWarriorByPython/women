from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


def pageNotFound(request, exception):
    return HttpResponse('<h1>Sorry, but something went wrong, see you later!</h1>')


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'The main page',
        'cat_selected': 0
    }
    return render(request, 'women/index.html',context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About the site'
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id={post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html',context=context)