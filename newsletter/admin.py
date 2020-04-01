from django.contrib import admin
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

# Register your models here.
admin.site.register(Newsletter, NewsletterAdmin)


