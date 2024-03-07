from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    # get customers statistics and details
    products = Product.objects.all()
    customers = Customer.objects.all()
    customersCount = customers.count()
    
    # get order statistics and details
    orders = Order.objects.all()
    ordersCount = orders.count()
    deliveredCount = Order.objects.filter(status = 'Delivered').count()
    pendingCount = Order.objects.filter(status = 'Pending').count()
    
    
    context = {'products': products, 'customers': customers,'customersCount':customersCount,'deliveredCount': deliveredCount,'orderCount': ordersCount,'pendingCount': pendingCount,'orders': orders}
    
    return render(request, 'accounts/dashboard.html',context)


def products(request):
    
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)




def customer(request):
    return render(request, 'accounts/customer.html')