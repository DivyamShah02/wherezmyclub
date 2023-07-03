from django.db import models

# Create your models here.

class userData(models.Model):
    entered = models.BooleanField(default=False)
    user_id = models.CharField(max_length=4,default=0)
    user_name = models.CharField(max_length=255,default=0)
    user_email = models.EmailField(max_length=255,default=0)
    user_number = models.CharField(max_length=20,default=0)
    user_pass_qty = models.CharField(max_length=2,default=0)
    user_pass_amt = models.CharField(max_length=10,default=0)
    user_qr = models.ImageField(upload_to='user_qrs')
    payment_id = models.CharField(default=0,max_length=255)