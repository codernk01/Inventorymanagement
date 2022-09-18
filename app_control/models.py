from django.db import models

class Factory(models.Model):
    
    factory_name = models.CharField( max_length=50,null=False)
    factory_location=models.CharField(max_length=50)

    def __str__(self):
        return self.factory_name

# Create your models here.
class Inventory(models.Model):
    
    product_name = models.CharField( max_length=50,null=True,blank=True)
    product_quantity = models.PositiveIntegerField(null=True,blank=True)
    product_price = models.DecimalField( max_digits=10, decimal_places=2,null=True,blank=True)
    product_description = models.CharField(max_length=100,null=True,blank=True)
    product_Img = models.ImageField(upload_to='images/',null=True, blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='products',default='1',null=True,blank=True)
    def __str__(self):
        return self.product_name