# from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name='movies'

urlpatterns = [
    path('',views.movie_list,name="list"),
    path('create/',views.movie_create,name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.movie_detail,name="detail"),
]