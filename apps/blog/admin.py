from django.contrib import admin
from apps.blog.models import BlogPost, BlogCategory

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_added']
    list_filter = ('date_added', 'category')
    search_fields = ['title', 'body', 'category__name']
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(BlogPost, BlogPostAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(BlogCategory, BlogCategoryAdmin)
