from django.contrib import admin

from .models import Category, Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'version_no', 'docfile', 'category', 'get_format', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'document_count', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
