from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('categories_grid/', views.categories_grid, name='categories_grid'),
    path('details_post_default/', views.details_post_default, name='details_post_default'),
    path('details_post_review/', views.details_post_review, name='details_post_review'),
    path('contact/', views.contact, name='contact'),
    path('typography/', views.typography, name='typography'),
    #path('articles/', views.article_list, name='base' ),
]
