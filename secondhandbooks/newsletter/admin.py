from django.contrib import admin
from .models import SubscribedUsers

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
    )

    ordering = ('name',)

admin.site.register(SubscribedUsers, NewsletterAdmin)    