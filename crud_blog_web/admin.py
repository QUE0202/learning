from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Pola w formularzu (poprawione)
    fieldsets = [
        ('Informacje o artykule', {'fields': ['title', 'year', 'content', 'image']}),
    ]
    # Pola w liście
    list_display = ['title', 'year']
    # Pole filtra
    list_filter = ['year']
    # Pole wyszukiwarki
    search_fields = ['title', 'content']