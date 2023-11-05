from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50, null=True)
    product_description = models.CharField(max_length=500)
    product_quantity = models.PositiveIntegerField(null=True)
    product_price = models.FloatField(null=True)
    product_sales = models.FloatField(null=True)

    def __str__(self):
        return f'{self.product_name}'


