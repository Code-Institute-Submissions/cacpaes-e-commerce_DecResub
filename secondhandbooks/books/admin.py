from django.contrib import admin

from .models import Book, Category, Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'author'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'details',
    )    


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)