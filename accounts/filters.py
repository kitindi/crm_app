import django_filters

from django import forms
from .models import *
from django.forms.widgets import TextInput,EmailInput,DateInput,Select,NumberInput

class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product 
        fields =['product_category','product_name','brand']
        
        
         
       
  
        