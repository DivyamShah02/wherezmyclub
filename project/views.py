
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
import random,datetime,json
from PIL import Image
from user_info.models import userData
from django.core.files.uploadedfile import InMemoryUploadedFile
import qrcode
import io


def admin_boss(request):
    return redirect('http://127.0.0.1:8000/admin')

def home(request):
    return render(request,'index.html')

def payment_success(request):
    try:
        try:
            contact_name = request.COOKIES.get('contact_name')
            contact_email = request.COOKIES.get('contact_email')
            mobile_number = request.COOKIES.get('mobile_number')
            pass_count= request.COOKIES.get('pass_count')
        except:
            return redirect('generated_pass')
        try:
            payment_id = request.GET.get('payment_id')
        except:
            return redirect('error')
        new_id = True
        while new_id:
            uid = random.randint(1111,9999)
            if len(userData.objects.filter(user_id = uid)) == 0:
                new_id = False
        
        username = f'http://127.0.0.1:8000/qr_check/{uid}'
        qr = qrcode.QRCode(version=1, box_size=10, border=1)
        qr.add_data(username)
        qr.make(fit=True)
        image = qr.make_image(fill_color='black', back_color='white')
        user_data = userData(user_id=uid, user_name = contact_name,user_email=contact_email,user_number=mobile_number,user_pass_qty=pass_count)
        image_io = io.BytesIO()
        image.save(image_io, format='PNG')
        image_file = InMemoryUploadedFile(
            image_io,
            None,
            f'{contact_name}.png',
            'image/png',
            image_io.tell(),
            None
        )
        user_data.user_qr = image_file
        user_data.save()
        

        
        response = redirect('generated_pass')
        response.set_cookie('user_id',uid,max_age=15*24*60*60)
        response.delete_cookie('contact_name')
        response.delete_cookie('contact_email')
        response.delete_cookie('mobile_number')
        response.delete_cookie('pass_count')
        
        return response
    except:
        return redirect('error')

def generated_pass(request):
    try:
        user_id = request.COOKIES.get('user_id')
        user_data = userData.objects.filter(user_id=user_id)[0]
        data = {
            'qr':user_data.user_qr.url,
            'pass_qty':user_data.user_pass_qty,
            'name':user_data.user_name,
        }
        return render(request,'ticket.html',data)
    except:
        return redirect('home')
   
@login_required(login_url=reverse_lazy('admin_boss'))
def qr_check(request,id):
    user_data = userData.objects.filter(user_id=id)
    if len(user_data) == 0:
        return render(request,'no_entry.html')
    elif user_data[0].entered:
        return render(request,'entered.html')
    else:
        user_obj = userData.objects.get(user_id=id)
        user_obj.entered = True
        user_obj.save()
        data = {
            'user_name' : user_data[0].user_name,
            'people' : user_data[0].user_pass_qty,
            'mobile_number' : user_data[0].user_number,
        }
        return render(request,'entry.html',data)
    
def error(request):
    return HttpResponse('<h1>Error Occured!<br>Please contact - </h1>')