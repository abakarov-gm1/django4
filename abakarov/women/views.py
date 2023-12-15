from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


data_db = [
    {'id': 1, 'name': 'Babatov', 'age': 14, 'Work': True},
    {'id': 2, 'name': 'Varlamov', 'age': 14, 'Work': False},
    {'id': 3, 'name': 'Tagirov', 'age': 24, 'Work': False},
    {'id': 4, 'name': 'Filatov', 'age': 44, 'Work': False},
    {'id': 5, 'name': 'Footler', 'age': 64, 'Work': True},
    {'id': 6, 'name': 'Brovn', 'age': 4, 'Work': True},
]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': 'King',
            'body': 'its Home Page',
            'float': 24.56,
            'obj': Test(10, 20),
            'mass': data_db,
            'menu': [{'id': 1, 'name': 'О сайте', 'link': "14"},
                     {'id': 1, 'name': 'Добавить статью', 'link': "14"},
                     {'id': 1, 'name': 'Обратная связь', 'link': "14"},
                     {'id': 1, 'name': 'Войти', 'link': "14"},
                     ]
    }

    return render(request, 'women/index.html', data)


def about(request):
    return render(request, 'about/index.html')


def error404(request, exception):
    return HttpResponseNotFound('<h1 style={color:blue}> Страница не найдена </h1>')


def posts(request, id):
    return HttpResponse(f"<h1> Номер поста - {id}</h1>")
    # return render(request, 'posts/index.html')

