import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        #fields = '__all__)'
        fields = ['product','status']
        #exclude = ['customer','date_created']