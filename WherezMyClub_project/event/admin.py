from django.contrib import admin
from event.models import EventData

# Register your models here.
class AdminEventData(admin.ModelAdmin):
    list_display = ('event_name','event_venue','event_date','event_time')
admin.site.register(EventData,AdminEventData)