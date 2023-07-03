from django.contrib import admin
from user_info.models import userData

# Register your models here.

class AdminUserData(admin.ModelAdmin):
    list_display=('user_id','entered','user_name','payment_id','user_email','user_pass_qty','user_number','user_qr')
    
admin.site.register(userData,AdminUserData)
