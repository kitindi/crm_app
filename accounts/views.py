from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .filters import ProductFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from authentication.decorators import allowed_user
# Create your views here.

@login_required

def home(request):
    # get customers statistics and details
    products = Product.objects.filter(user=request.user)
    customers = Customer.objects.filter(user=request.user)
    customersCount = customers.count()
    
    # get order statistics and details
    orders = Order.objects.filter(user=request.user)
    ordersCount = orders.count()
    deliveredCount = Order.objects.filter(status = 'Delivered').count()
    pendingCount = Order.objects.filter(status = 'Pending').count()
    
    
    context = {'products': products, 'customers': customers,'customersCount':customersCount,'deliveredCount': deliveredCount,'orderCount': ordersCount,'pendingCount': pendingCount,'orders': orders}
    
    return render(request, 'accounts/dashboard.html',context)

# Products APIs


# create a new product
@login_required
def create_product(request):
    form = ProductForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            # connecting product with the user of the task
            product.user = request.user
            product.save()
            return redirect('products')
      
        
    return render(request, 'accounts/product_form.html', context)



# fetch all products
@login_required
def products(request):
    # user_products = request.user.product
    products = Product.objects.filter(user=request.user)
       
    context = {'products': products}
    return render(request, 'accounts/products.html', context)

# view product details
@login_required
def product_details(request, pk):
    product = Product.objects.get(id=pk, user=request.user)
    # get number of products orders
    
    orders = product.order_set.filter(user=request.user)
    orderCount = orders.count()
    paidOrder = product.order_set.filter(status = 'Delivered').count()
    
    # calculate total amount of sales for paid orders
    
    totalSales = 0
    
    for order in orders:
        if order.status == 'Delivered':
            totalSales += (order.quantity * order.product.price)
    
    context = {'product': product,'orderCount': orderCount,'paidOrder': paidOrder,'totalSales': totalSales}
   
    
    return render(request, 'accounts/product_details.html', context)

# edit product
@login_required
def edit_product(request,pk):
    
    product = Product.objects.get(id=pk, user=request.user)
    form = ProductForm(instance=product)
    context = {'form': form}
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            # connecting product with the user of the task
            product.user = request.user
            product.save()
            
            return redirect('products')
    
    return render(request, 'accounts/edit_product.html', context)




# delete a product
@login_required
def delete_product(request,pk):
    # get the instance of the product to delete
    
    product = Product.objects.get(id=pk,user=request.user)
    product.delete()
    
    return redirect('products')
    
    
    
    



@login_required
def customer(request, pk):
    # get a customer details
    customer = Customer.objects.get(id=pk,user=request.user)
    
    # get all customer orders
    orders = customer.order_set.filter(user=request.user)
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

# get all customers
@login_required
def all_customers(request):
    customers = Customer.objects.filter(user=request.user)
    
    return render(request, 'accounts/customers.html',{'customers': customers})   
# create new customer
@login_required
def add_customer(request):
    form = CustomerForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            
            return redirect('home')
    
    return render(request, 'accounts/customer_form.html', context)



# update customer customer data
@login_required
def update_customer(request,pk):
    
    customer = Customer.objects.get(id=pk, user=request.user)
    form = CustomerForm(instance=customer)
    context = {'form': form}
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            
            return redirect('home')
    
    return render(request, 'accounts/update_customer.html', context)


# delete customer
@login_required
def delete_customer(request,pk):
    
    customer = Customer.objects.get(id=pk, user=request.user)
    customer.delete()
    
    return redirect('home')
    
# handling customer orders

# Creating customer order

@login_required
def create_order(request, pk):
    customer = Customer.objects.get(id=pk, user=request.user)
    form = OrderForm(initial={'customer': customer})
    context = {'form': form}
    
    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user)
        
        if form.is_valid():
            
            order = form.save(commit=False)
            
            order.user = request.user
            order.save()
            return redirect('home')
    return render(request, 'accounts/order_form.html', context)

# Update order information
@login_required
def update_order(request, pk):
    # get the order instance
    order = Order.objects.get(id=pk, user=request.user)
    form = OrderForm(instance=order)
    context = {'form': form}
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order,)
        if form.is_valid():
            order = form.save(commit=False)
            
            order.user = request.user
            order.save()
            
            return redirect('home')
    
    return render(request, 'accounts/update_order.html', context)

# delete order information
@login_required
def delete_order(request,pk):
    
    order = Order.objects.get(id=pk, user=request.user)
    order.delete()
    
    return redirect('home')
    
    
# Handling products logic

