from django.db import models

# Create your models here.

class EventData(models.Model):
    # Auto generated
    event_id = models.CharField(max_length=10) 
    user_id = models.CharField(max_length=10) 
    
    # Basic Info
    event_name = models.CharField(max_length=255)
    event_desc = models.TextField()
    event_venue = models.CharField(max_length=255,default='Null')
    event_date = models.CharField(max_length=100,default='Null')
    event_time = models.CharField(max_length=100,default='Null')
    event_date_alt = models.CharField(max_length=100,default='Null')
    event_time_alt = models.CharField(max_length=100,default='Null')
    flyer = models.ImageField(upload_to='Flyer')
    table_chart = models.ImageField(upload_to='Table_Chart')
    
    host = models.CharField(max_length=255)
    collaborator = models.CharField(max_length=255,default='Null')
    free_gl = models.BooleanField(default=False)
    paid_gl = models.BooleanField(default=False)
    pass_price = models.CharField(max_length=10,default=0)
    token_price = models.CharField(max_length=10,default=0)
    max_pass = models.CharField(max_length=10,default=15)
    
    # Good Things
    gt_1 = models.CharField(max_length=255,default='Null')
    gt_2 = models.CharField(max_length=255,default='Null')
    gt_3 = models.CharField(max_length=255,default='Null')
    gt_4 = models.CharField(max_length=255,default='Null')
    gt_5 = models.CharField(max_length=255,default='Null')
    
    
    #Extra Points
    pt1_head = models.CharField(max_length=50,default='Null')
    pt1_value = models.CharField(max_length=50,default='Null')
    
    pt2_head = models.CharField(max_length=50,default='Null')
    pt2_value = models.CharField(max_length=50,default='Null')
    
    pt3_head = models.CharField(max_length=50,default='Null')
    pt3_value = models.CharField(max_length=50,default='Null')
    
    pt4_head = models.CharField(max_length=50,default='Null')
    pt4_value = models.CharField(max_length=50,default='Null')
    
    pt5_head = models.CharField(max_length=50,default='Null')
    pt5_value = models.CharField(max_length=50,default='Null')
    
    pt6_head = models.CharField(max_length=50,default='Null')
    pt6_value = models.CharField(max_length=50,default='Null')
    
    