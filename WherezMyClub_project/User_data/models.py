from django.db import models

# Create your models here.

class Club_Company(models.Model):
    user_id = models.CharField(max_length=10)
    acc_type = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    club_name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=100,default='Null')
    email = models.CharField(max_length=255)
    instagram_link = models.CharField(max_length=255,default='Null')
    address = models.TextField()
    number = models.CharField(max_length=12)
    logo = models.ImageField(upload_to='Logos')
    activated = models.BooleanField(default=False)

class Couple(models.Model):
    user_id = models.CharField(max_length=10)
    event_id = models.CharField(max_length=10)
    
    his_first_name = models.CharField(max_length=255)
    his_last_name = models.CharField(max_length=255)
    his_number = models.CharField(max_length=12)
    
    her_first_name = models.CharField(max_length=255)
    her_last_name = models.CharField(max_length=255)
    her_number = models.CharField(max_length=12)
    
    email = models.CharField(max_length=255)
    user_qr = models.ImageField(upload_to='couple')
    pass_qty = models.CharField(max_length=5)
    entered = models.BooleanField(default=False)
    
    

class Stag(models.Model):
    user_id = models.CharField(max_length=10)
    event_id = models.CharField(max_length=10)
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)    
    email = models.CharField(max_length=255)
    number = models.CharField(max_length=12)    
    user_qr = models.ImageField(upload_to='stag')
    pass_qty = models.CharField(max_length=5)
    entered = models.BooleanField(default=False)    
    

class Message(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()