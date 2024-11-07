from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    eligibility = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
