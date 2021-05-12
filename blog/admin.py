from django.contrib import admin
from .models import Post, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'published', 'author', 'rubric')
    list_display_links = ('title', 'body')
    search_fields = ('title', 'body', 'published', 'author', 'rubric')
 
admin.site.register(Post, BbAdmin)
admin.site.register(Rubric)
