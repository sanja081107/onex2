from django.contrib import admin
from .models import *

class NotebookAdmin(admin.ModelAdmin):
    list_display = ('width', 'depth', 'height', 'title')
    list_display_links = ('title',)

admin.site.register(Brand)
admin.site.register(Notebook, NotebookAdmin)

