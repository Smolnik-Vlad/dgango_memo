from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import product as prod


# Create your views here. для объявлений функций эндпоинтов

def index(request):
  s = 'Список объявлений\r\n\r\n\r\n'
  for bb in prod.objects.order_by('-published'):
    s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
  return HttpResponse(s, content_type='text/plain; charset=utf-8')

def nextPage(request):
    return HttpResponse("next page")

def first(request):
    return render(request, 'first.html') # отображает страницу

class ClassEndpointView(TemplateView):              #Пример класса-эндпоинта
    template_name = 'first.html'


    #Изучить все методы запроса с TemplateView