from django.db import models  
  
class Customer(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)


class Product(models.Model):  
    pid = models.CharField(max_length=20)  
    pname = models.CharField(max_length=100)  
    pprice = models.IntegerField()
    class Meta:  
        db_table = "products" 

class Payment(models.Model):
    customer_id = models.CharField(max_length=20) 
    amount = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.customer_id, self.amount)

    class Meta:  
        db_table = "payments"