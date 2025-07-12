from django.contrib import admin
from .models import Book

#Customise for search, list and filter capabilitites

class BookAdmin(admin.ModelAdmin):
    # Show these fields as columns in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the right sidebar for quick filtering
    list_filter = ('author', 'publication_year')
    
    # Include a search box to search by title and author fields
    search_fields = ('title', 'author')


# Register your models here.
admin.site.register(Book, BookAdmin)