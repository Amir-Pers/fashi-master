from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'counted_view', 'published_date', 'created_date']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty'
    list_filter = ('author', 'status', 'category')
    search_fields = ['title', 'content']

    class Meta:
        ordering = ['-created_date']


admin.site.register(Post, PostAdmin)
