from django.contrib import admin

# Register your models here.

from .models import *
""" 
from .models import Customer
from .models import Product
from .models import Order
from .models import Tag """

admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)