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
    deliveredCount = customer.order_set.filter(status = 'Delivered').count()
    orderCount = orders.count()
    subTotal = 0
    
    if orders.count() > 0:
        for order in orders:
            subTotal += order.quantity * order.product.price
    else:
        subTotal = 0
  
    
    context = {'customer':customer,'orderCount':orderCount,'deliveredCount':deliveredCount,'subTotal':subTotal,'orders':orders,'deliveredCount':deliveredCount}
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
    
    return render(request, 'accounts/update_customer.html', context)


# delete customer

def delete_customer(request,pk):
    
    customer = Customer.objects.get(id=pk)
    customer.delete()
    
    return redirect('home')
    
# handling customer orders

# Creating customer order


def create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer': customer})
    context = {'form': form}
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'accounts/order_form.html', context)

# Update order information


def update_order(request, pk):
    # get the order instance
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    
    return render(request, 'accounts/update_order.html', context)

# delete order information

def delete_order(request,pk):
    
    order = Order.objects.get(id=pk)
    order.delete()
    
    return redirect('home')
    
    
# Handling products logic

