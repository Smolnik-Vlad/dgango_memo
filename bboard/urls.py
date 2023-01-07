from django.urls import path

from bboard.views import index, nextPage, get_obj_by_id

urlpatterns =[
    path('', index),
    path('nextPage', nextPage),
    path('get_obj_by_id/<int:obj_id>/', get_obj_by_id)
]