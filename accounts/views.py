from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

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




def customer(request, pk):
    # get a customer details
    customer = Customer.objects.get(id=pk)
    
    # get all customer orders
    orders = customer.order_set.all()
    orderCount = orders.count()
    
    context = {'customer':customer,'orderCount':orderCount,'orders':orders}
    return render(request, 'accounts/customer.html', context)

# create new customer

def add_customer(request):
    form = CustomerForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    
    return render(request, 'accounts/customer_form.html', context)



# update customer customer data

def update_customer(request,pk):
    
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    context = {'form': form}
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    
    return render(request, 'accounts/customer_form.html', context)


# delete customer

def delete_customer(request,pk):
    
    customer = Customer.objects.get(id=pk)
    customer.delete()
    
    return redirect('home')
    
