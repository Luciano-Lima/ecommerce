from django.contrib import admin
from .models import Order, ProductOrdered

# Register your models here.
class OrderInline(admin.TabularInline):
    model = ProductOrdered

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderInline, )

admin.site.register(Order, OrderAdmin)