from django.contrib import admin
from .models import Article

# Register your models here.
""" @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
 """
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)
    ordering = ('-published_date',)

admin.site.register(Article, ArticleAdmin)
