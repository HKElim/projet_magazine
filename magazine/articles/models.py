from django.db import models

# Create your models here.

CATEGORY_CHOICES={
    ('GA','Gaming'),
    ('PL','Platform'),
    ('PA','Playstation'),
    ('HA','Hardware'),
}

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, blank=True)
    content = models.TextField()
    description = models.TextField(blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    image_article = models.ImageField(upload_to='articles', blank=True)

    def __str__(self):
        return self.title