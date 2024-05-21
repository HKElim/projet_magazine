from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('categories_grid/', views.categories_grid, name='categories_grid'),
    path('details_post_default/<int:pk>', views.Article_detail.as_view(), name='details_post_default'),
    path('details_post_review/', views.details_post_review, name='details_post_review'),
    path('contact/', views.contact, name='contact'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    #path('articles/', views.article_list, name='article' ),
]
