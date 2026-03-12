from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='products/',null=True,blank=True)
    stock=models.IntegerField()
    def __str__(self):
        return self.name
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.product.name
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.FloatField()
    def __str__(self):
        return self.product.name