"""secondhandbooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from books.models import Book
from secondhandbooks.sitemap import BookSitemap, CategorySitemap
from secondhandbooks.robots import robots_txt

sitemaps = {
    'blog':BookSitemap,
    'category': CategorySitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "secondhandbooks.views.error_400"
handler403 = "secondhandbooks.views.error_403"
handler404 = "secondhandbooks.views.page_not_found_view"
handler500 = "secondhandbooks.views.error_500"
