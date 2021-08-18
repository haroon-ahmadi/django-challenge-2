from django.contrib import admin
from app_1.models import Author, Book 
from django.utils.html import format_html

class BookInline(admin.TabularInline):
    model=Book


class AuthorAdmin(admin.ModelAdmin):
    inlines=[BookInline]
    @admin.display(description='Action')
    def book_list(self, obj):
       return format_html(f"<a href= '/book/list?author_name={ obj.name }'>View books list as user</a>")
    list_display = ( 'name','modified_at', 'created_at', 'book_list')
    readonly_fields = ()
    
        
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'modified_at', 'created_at')
    readonly_fields = ()

admin.site.register(Book, BookAdmin)