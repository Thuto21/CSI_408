from django.db import models

# Create your models here.
from django.db import models


class Staff(models.Model):
    staffid = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

