from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base' ),
    #path('articles/', views.article_list, name='base' ),
]
