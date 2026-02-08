from django.contrib import admin
from website.models import Contact, Newsletter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_date']
    date_hierarchy = 'created_date'
    list_filter = ('name', 'email')
    search_fields = ['name', 'message']

    class Meta:
        ordering = ['-created_date']


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_date', 'updated_date']
    date_hierarchy = 'created_date'


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)