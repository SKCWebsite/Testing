from django.db import models


class ContactUsQuery(models.Model):
    name = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    query = models.CharField(max_length=500)    

