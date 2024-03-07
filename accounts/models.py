from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=100,  null=True)
    lastname = models.CharField(max_length=100,  null=True)
    phone_number = models.CharField(max_length=100,  null=True)
    email = models.EmailField(max_length=100,  null=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    CATEGORIES = (('Consumer Electronics', 'Consumer Electronics'),('Home & Garden', 'Home & Garden'),('Men Clothings', 'Men Clothings'),('Accessories', 'Accessories'),('Shoes', 'Shoes'))
    
    product_name = models.CharField(max_length=200,null=True)
    product_category = models.CharField(max_length=200,null=True, choices=CATEGORIES)
    quantity = models.PositiveBigIntegerField(null=True)
    cost = models.DecimalField(max_digits=9,decimal_places=2, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,null=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.product_name} -- {self.product_category}"
        
    

    
class Order(models.Model):
    
    STATUS =(('Pending', 'Pending'),('Out of delivery', 'Out of delivery'),('Delivered', 'Delivered'))
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product= models.ForeignKey(Product,null=True, on_delete=models.SET_NULL) 
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    status = models.CharField(max_length=200,null=True, choices =STATUS)
    
    def __str__(self):
        return f"{self.status}"
  
    

    