from django.contrib import admin
from product.models import Customer
from product.models import Payment, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Product)