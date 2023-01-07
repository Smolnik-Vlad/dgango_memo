from django.urls import path

from bboard.views import index, nextPage

urlpatterns =[
    path('', index),
    path('nextPage', nextPage)
]