from django.db import models

# Create your models here.
class DataDiscription(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    
