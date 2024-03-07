from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'price',
        'stock',
        'image',
    ]

    list_display_links = [
        'title',
        'author',
    ]

    list_editable = [
        'price',
        'stock',
    ]
    list_filter = [
        'author',
        'price',
    ]


admin.site.register(Book, BookAdmin)