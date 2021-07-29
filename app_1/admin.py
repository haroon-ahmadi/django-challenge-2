from django.contrib import admin

from app_1.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_at', 'created_at')
    readonly_fields = ()


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_at', 'created_at')
    readonly_fields = ()


admin.site.register(Book, BookAdmin)
