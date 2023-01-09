from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    mobile = models.PositiveBigIntegerField(null=False,blank=False)

