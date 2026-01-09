from django.contrib import admin
from Myapplication.models import Data

# Customize admin display
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'address', 'mail')  # Columns to show
    list_display_links = ('name',)  # Make 'name' clickable
    search_fields = ('name', 'mail', 'contact')  # Add search bar
    list_per_page = 10  # Pagination