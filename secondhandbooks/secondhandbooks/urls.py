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
from books.models import Book


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('accounts/', include('allauth.urls')),
    path('newsletter/', include('newsletter.urls')),
    url(r'^robots.txt$', TemplateView.as_view(template_name="static/robots.txt", content_type='text/plain')),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name="static/sitemap.xml", content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = "secondhandbooks.views.handler400"
handler403 = "secondhandbooks.views.handler403"
handler404 = "secondhandbooks.views.handler404"
handler500 = "secondhandbooks.views.handler500"
