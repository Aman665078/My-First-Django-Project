from django.db import models

class Record(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    phone_number = models.CharField(max_length=50)
    address =models.CharField(max_length=500)
    city = models.CharField( max_length=150)
    province = models.CharField( max_length=150)
    country = models.CharField(max_length=100)

    def __str__(self):
        
        return f"{self.first_name}   {self.last_name}"
