from django.contrib import admin
from django.urls import path
from WherezMyClub_project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # --- Admin --- #
    path('admin/', admin.site.urls),
    path('check_users/',views.check_users,name='check_users'),
    path('user_activate/<id>',views.user_activate,name='user_activate'),
    
    # --- Web Pages --- #
    path('',views.home,name='home'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('events/',views.events,name='events'),
    
    # -- Event Pages --- #
    path('event/<id>',views.event,name='event'),
    path('event_adder/',views.event_adder,name='event_adder'),
    path('event_edit/<id>',views.event_edit,name='event_edit'),
    path('event_report/<id>',views.event_report,name='event_report'),
    
    # --- Club & Company --- #
    path('register/',views.register,name='register'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='log_out'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('qr_check/stag/<eid>/<uid>',views.qr_check_stag,name='qr_check_stag'),
    path('qr_check/couple/<eid>/<uid>',views.qr_check_couple,name='qr_check_couple'),
    
    # --- User Pages --- #
    path('generated_pass/stag/<uid>',views.generated_pass_stag,name='generated_pass_stag'),
    path('generated_pass/couple/<uid>',views.generated_pass_couple,name='generated_pass_couple'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
