from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineAdminInline(admin.TabularInline):
    """
    TabularInline subclass defines the template used to render
    the Order in the admin interface. StackInline is another
    option.
    """
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    """
    The admin interface has the ability to edit more that one
    model on a single page.  This is known as inlines.
    """
    inlines = (OrderLineAdminInline, )
    
admin.site.register(Order, OrderAdmin)

