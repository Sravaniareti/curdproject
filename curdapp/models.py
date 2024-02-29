from django.db import models

class StudentaData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    contact=models.BigIntegerField()
    email=models.CharField(max_length=50)
    date=models.DateField()

# Create your models here.
