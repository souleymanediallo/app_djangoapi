from django.contrib import admin
from .models import Book, BookNumber, Character, Author
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


class BookNumberAdmin(admin.ModelAdmin):
    list_display = [
        'isbn_10',
        'isbn_13',
    ]

    list_display_links = [
        'isbn_10',
        'isbn_13',
    ]


admin.site.register(BookNumber, BookNumberAdmin)


class CharacterAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'book',
    ]

    list_display_links = [
        'name',
        'book',
    ]


admin.site.register(Character, CharacterAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'surname',
    ]

    list_display_links = [
        'name',
        'surname',
    ]

    list_filter = [
        'name',
        'surname',
    ]


admin.site.register(Author, AuthorAdmin)