from django.contrib import admin
from .models import Order, Product_Ordered

# Register your models here.
class OrderInline(admin.TabularInline):
    model = Product_Ordered

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderInline, )

admin.site.register(Order, OrderAdmin)