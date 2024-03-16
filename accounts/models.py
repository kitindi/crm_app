from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=100,  null=True)
    lastname = models.CharField(max_length=100,  null=True)
    phone_number = models.CharField(max_length=100,  null=True)
    location = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=100,  null=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    



class Product(models.Model):
    CATEGORIES = (('Consumer Electronics', 'Consumer Electronics'),('Home & Garden', 'Home & Garden'),('Men Clothings', 'Men Clothings'),('Accessories', 'Accessories'),('Shoes', 'Shoes'))
    
    product_name = models.CharField(max_length=200,null=True)
    product_category = models.CharField(max_length=200,null=True, choices=CATEGORIES)
    instock = models.PositiveBigIntegerField(null=True)
    reorder_level = models.PositiveIntegerField(null=True)
    cost = models.DecimalField(max_digits=9,decimal_places=2, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,null=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    brand = models.CharField(max_length=200,null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.product_name}"
        
    

    
class Order(models.Model):
    
    STATUS =(('Pending', 'Pending'),('Out of delivery', 'Out of delivery'),('Delivered', 'Delivered'))
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product= models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_ordered= models.DateField(null=True)
    quantity= models.PositiveBigIntegerField(null=True)
    date_delivered= models.DateField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    status = models.CharField(max_length=200,null=True, choices =STATUS)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.status}"
  
    

class Profile(models.Model):
    GENDER = (('Male','Male'), ('Female','Female'),('Rather not say','Rather not say'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=300, null=True)
    gender = models.CharField(max_length=100, choices =GENDER, null = True)
    phone_number = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    bio = models.TextField()
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    
    def __str__(self):
        return self.fullname
    
  
    