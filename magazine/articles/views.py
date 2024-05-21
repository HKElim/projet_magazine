from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import CATEGORY_CHOICES, Article

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "articles/home.html", {})

def categories_grid(request, *args, **kwargs):
    articles = Article.objects.all()
    return render(request, "articles/categories_grid.html", {'articles': articles})

class Article_detail(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return render(request, "articles/details_post_default.html", {'article': article})

def details_post_review(request, *args, **kwargs):
    return render(request, "articles/details_post_review.html", {})

def contact(request, *args, **kwargs):
    return render(request, "articles/contact.html", {})

def categories(request, *args, **kwargs):
    return render(request, "articles/categories_liste.html", {})

"""def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})"""

class CategoryView(View):
     def get(self, request, val):
        articles = Article.objects.filter(category=val)
        return render(request, "articles/categories_grid.html", locals())



""" def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})"""
