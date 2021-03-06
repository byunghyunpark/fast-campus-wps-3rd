from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^bookmark/add/$', views.add_bookmark, name='add_bookmark'),
    url(r'^bookmark/list/$', views.bookmark_list, name='bookmark_list'),
]
