from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, unique=True)
    pin_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField()

    image = models.ImageField(
        upload_to='products/'
    )

    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name}"



class Order(models.Model):

    PAYMENT_METHODS = (
            ('COD', 'Cash on Delivery'),
            
            ('Razorpay', 'Razorpay'),
    )

    STATUS_CHOICES = (

            ('Pending', 'Pending'),
        
            ('Processing', 'Processing'),

            ('Confirmed', 'Confirmed'),

            ('Shipped', 'Shipped'),

            ('Delivered', 'Delivered'),

            ('Cancelled', 'Cancelled'),
     )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order{self.id} by {self.user.username}"
    



    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.product.name} in Order {self.order.id}"


class Tracking(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tracking for Order {self.order.id}"
