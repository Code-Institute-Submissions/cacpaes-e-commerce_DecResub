from books.models import Book, Category
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap


class BookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Book.objects.all()

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def location(self,obj):
        return '/?category=%s' % (obj.name)    