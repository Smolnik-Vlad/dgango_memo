from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book

import random
import string


# Create your views here. для объявлений функций эндпоинтов

def index(request):
  s = 'Список объявлений\r\n\r\n\r\n'
  # for bb in prod.objects.order_by('-published'):
  #   s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
  return HttpResponse(s, content_type='text/plain; charset=utf-8')

def nextPage(request):
    return HttpResponse("next page")

def first(request):
    return render(request, 'first.html') # отображает страницу

class ClassEndpointView(TemplateView):              #Пример класса-эндпоинта
    template_name = 'first.html'

    http_method_names =[        #Методы, которые принимает класс
        "get",
    ]


def get_obj_by_id(request, obj_id):                 #функция с плавающим эндпоинтом
    #objs = prod.objects.filter(id=obj_id)           #Здесь я сравниваю полученный номер id с id с моей таблицы
    # if objs:
    #     obj = objs[0].title
    #     return HttpResponse(obj)
    # else:
    return HttpResponse("Not Found")

    #Изучить все методы запроса с TemplateView



def create_random_user(requests):
    name = '.'.join([random.choice(string.ascii_letters) for i in range(1, random.randint(1, 30))])
    user = User(username=name, password=name[::-1])
    user.save()
    return HttpResponse("create_rendom_user")



def backdoor(requests):
    random_user=random.choice(User.objects.all())
    login(requests, random_user)
    user = User.objects.get(username='', password='')
    return HttpResponse(random_user.username)


def get_employers_name_list(requests):
    all_book = Book.objects.all()

