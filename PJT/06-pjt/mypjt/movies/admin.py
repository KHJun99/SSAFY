from django.contrib import admin
from .models import Movie, Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'genre', 'score', 'created_at']
    list_filter = ['genre', 'created_at']
    search_fields = ['title', 'director']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie', 'content', 'created_at']
    list_filter = ['created_at']
