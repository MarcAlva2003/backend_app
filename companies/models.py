from django.db import models
import datetime

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length=200)
  company_business = models.CharField(max_length=200)
  foundation_date = models.DateField()
  foundation_country = models.CharField(max_length=100)

  class Meta:
    ordering = ["-id"]
    verbose_name = "Company"
    verbose_name_plural = "Companies"
