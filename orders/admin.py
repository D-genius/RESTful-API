from django.contrib import admin
from .models import Customer, Order

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','code']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','item','amount','time']
    search_fields = ['item']