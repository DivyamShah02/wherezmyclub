from django.contrib import admin
from User_data.models import Couple,Stag,Club_Company,Message

# Register your models here.

class AdminCouple(admin.ModelAdmin):
    list_display=('user_id','his_first_name','his_last_name','her_first_name','her_last_name','email') 
admin.site.register(Couple,AdminCouple)

class AdminStag(admin.ModelAdmin):
    list_display=('user_id','first_name','last_name','email')
admin.site.register(Stag,AdminStag)  

class AdminClubCompany(admin.ModelAdmin):
    list_display=('email','acc_type','club_name','company_name')
admin.site.register(Club_Company,AdminClubCompany)

class AdminMessage(admin.ModelAdmin):
    list_display=('name','company','email','message')
admin.site.register(Message,AdminMessage)