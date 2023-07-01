"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.home,name='home'),
    path('payment_success/',views.payment_success,name='payment_success'),
    path('generated_pass/',views.generated_pass,name='generated_pass'),
    path('qr_check/<int:id>',views.qr_check,name='qr_check'),
    path('admin_boss/',views.admin_boss,name='admin_boss'),
    path('error/',views.error,name='error'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
