from django.shortcuts import render, get_object_or_404
#from .models import Article

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "articles/home.html", {})

def categories_grid(request, *args, **kwargs):
    return render(request, "articles/categories_grid.html", {})

def details_post_default(request, *args, **kwargs):
    return render(request, "articles/details_post_default.html", {})

def details_post_review(request, *args, **kwargs):
    return render(request, "articles/details_post_review.html", {})

def contact(request, *args, **kwargs):
    return render(request, "articles/contact.html", {})

def typography(request, *args, **kwargs):
    return render(request, "articles/typography.html", {})

"""def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})"""
