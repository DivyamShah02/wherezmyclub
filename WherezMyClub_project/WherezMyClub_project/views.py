#Admin credentials username - 'admin' pass- 'admin'
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
import random,qrcode,io,datetime
from event.models import EventData
from User_data.models import Couple,Stag,Club_Company,Message

## ------ Web Pages ------ ##
def home(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    all_event_data = EventData.objects.all()
    all_event_data = list(reversed(all_event_data))
    
    data = {
        'all_event_data':all_event_data[0:3],
        'logged_in':logged_in,
    }
    return render(request,'index.html',data)

def contact_us(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    success = 0
    if request.method == 'POST':
        new_message = Message(
            name = request.POST.get('contact-name'),
            company = request.POST.get('contact-company'),
            email = request.POST.get('contact-email'),
            message = request.POST.get('contact-message'),
        )
        new_message.save()
        success = 1
    data = {
        'logged_in':logged_in,
        'success':success,
    }
    return render(request,'contact_us.html',data)

def events(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    all_event_data = EventData.objects.all()
    all_event_data = list(reversed(all_event_data))
    
    data = {
        'all_event_data':all_event_data,
        'logged_in':logged_in,
    }
    return render(request,'events.html',data)

## ------ Club & Company ------ ##
def register(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    success = 0
    if request.method == 'POST':
        email = request.POST.get('email')
        user_exist = Club_Company.objects.filter(email=email)
        if len(user_exist) == 0:
            if request.POST.get('acc_type') == 'Club':
                company_name = 'Null'
                club_name = request.POST.get('club_name')
            elif request.POST.get('acc_type') == 'Company':
                club_name = 'Null'     
                company_name = request.POST.get('company_name')                       
            new_id = True
            while new_id:
                uid = random.randint(1111111111,9999999999)
                if len(Club_Company.objects.filter(user_id = uid)) == 0:
                    new_id = False
            
            user = User.objects.create_user(username=uid,email=email,password=request.POST.get("password"))
            user.save()            
            new_acc = Club_Company(
                user_id = uid,
                acc_type = request.POST.get('acc_type'),
                company_name = company_name,
                club_name = club_name,
                gst_number = request.POST.get('gst_number'),
                email = request.POST.get('email'),
                instagram_link = request.POST.get('instagram'),
                address = request.POST.get('address'),
                number = request.POST.get('number'),
                logo = request.FILES.get('logo'),
            )
            new_acc.save()
            user_log = authenticate(request, username=uid, password=request.POST.get("password"))
            login(request,user_log)
            return redirect('dashboard')
            success = 1 # User Created
        else:
            success = 2 # User Already Exist        
        
    data = {
        'success':success,
        'logged_in':logged_in,
    }
    return render(request,'register.html',data)

def log_in(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    error = 0
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_info = User.objects.filter(email=email)
            if len(user_info) > 0:
                username = user_info[0] # It is an object that stores user id
                user = authenticate(request, username=username, password=password) # Authenticating user
                if user is not None:
                    # User is authenticated
                    login(request, user)
                    request.session.set_expiry(30 * 24 * 60 * 60) # Storing user data in session (remembering the user)
                    return redirect('dashboard')
                else:
                    error = 1 # Wrong password
            else:
                error = 2 # Not registered
    except:
        error = 3 # fatal error
    data = {
        'error':error,
        'logged_in':logged_in,
    }
    return render(request,'login.html',data)

@login_required(login_url=reverse_lazy('login'))
def log_out(request):
    logout(request)
    return redirect('home') 

@login_required(login_url=reverse_lazy('login'))
def edit_profile(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    user = request.user
    user_data = Club_Company.objects.filter(user_id = user)[0]
    if request.method == 'POST':
        user_obg = Club_Company.objects.get(user_id=user)
        user_obg.company_name = request.POST.get('company_name')
        user_obg.club_name = request.POST.get('club_name')
        user_obg.gst_number = request.POST.get('gst_number')
        user_obg.email = request.POST.get('email')
        user_obg.instagram_link = request.POST.get('instagram')
        user_obg.address = request.POST.get('address')
        user_obg.number = request.POST.get('number')            
        user_obg.save()
        return redirect('dashboard')
        
    data = {
        'user':user,
        'user_data':user_data,
        'logged_in':logged_in,
    }
    return render(request,'edit_profile.html',data)

@login_required(login_url=reverse_lazy('login'))
def dashboard(request):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    try:
        user = request.user
        user_data = Club_Company.objects.filter(user_id=user)[0]
        event_data = EventData.objects.filter(user_id = user)
        if len(event_data) == 0:
            event_data = None
        data = {
            'user':user,
            'user_data':user_data,
            'event_data':event_data,
            'logged_in':logged_in,
        }    
        return render(request,'dashboard.html',data)
    except:
        return redirect('login')

## ------ Event Handler ------ ##
def event(request,id):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    event_data = EventData.objects.filter(event_id=id)
    if len(event_data) > 0:
        if request.method == 'POST':
            domain = request.META.get('HTTP_HOST')
            if request.POST.get('stag_first_name'):
                
                new_id = True
                while new_id:
                    uid = random.randint(1111111111,9999999999)
                    if len(Stag.objects.filter(user_id = uid)) == 0:
                        new_id = False
                
                link_data = f'https://{domain}/qr_check/stag/{event_data[0].event_id}/{uid}'
                
                qr = qrcode.QRCode(version=1, box_size=10, border=1)
                qr.add_data(link_data)
                qr.make(fit=True)
                image = qr.make_image(fill_color='black', back_color='white')
                new_stag = Stag(
                    user_id = uid,
                    first_name = request.POST.get('stag_first_name'),
                    last_name = request.POST.get('stag_last_name'),
                    email = request.POST.get('stag_email'),
                    number = request.POST.get('stag_number'),
                    pass_qty = request.POST.get('stag_pass_qty'),
                    event_id = event_data[0].event_id,
                )
                                
                image_io = io.BytesIO()
                image.save(image_io, format='PNG')
                image_file = InMemoryUploadedFile(
                    image_io,
                    None,
                    f'{uid}.png',
                    'image/png',
                    image_io.tell(),
                    None
                )
                new_stag.user_qr = image_file                
                
                new_stag.save()
                return redirect('generated_pass_stag',uid)
                
            elif request.POST.get('his_first_name'):
                new_id = True
                while new_id:
                    uid = random.randint(1111,9999)
                    if len(Couple.objects.filter(user_id = uid)) == 0:
                        new_id = False
                
                link_data = f'https://{domain}/qr_check/couple/{event_data[0].event_id}/{uid}'
                
                qr = qrcode.QRCode(version=1, box_size=10, border=1)
                qr.add_data(link_data)
                qr.make(fit=True)
                image = qr.make_image(fill_color='black', back_color='white')
                new_couple = Couple(
                    user_id = uid,
                    his_first_name = request.POST.get('his_first_name'),
                    his_last_name = request.POST.get('his_last_name'),
                    his_number = request.POST.get('his_number'),
                    her_first_name = request.POST.get('her_first_name'),
                    her_last_name = request.POST.get('her_last_name'),
                    her_number = request.POST.get('her_number'),
                    email = request.POST.get('couple_email'),
                    pass_qty = request.POST.get('couple_pass_qty'),                    
                    event_id = event_data[0].event_id,
                )
                                
                image_io = io.BytesIO()
                image.save(image_io, format='PNG')
                image_file = InMemoryUploadedFile(
                    image_io,
                    None,
                    f'{uid}.png',
                    'image/png',
                    image_io.tell(),
                    None
                )
                new_couple.user_qr = image_file                
                
                new_couple.save()
                return redirect('generated_pass_couple',uid)
                
        
        event_data = event_data[0]
        
        gt_data = [event_data.gt_1,event_data.gt_2,event_data.gt_3,event_data.gt_4,event_data.gt_5]
        
        data={
            'event_data':event_data,
            'gt_data':gt_data,
            'logged_in':logged_in,
        }
        return render(request,'event.html',data)
    else:
        return redirect('home')

@login_required(login_url=reverse_lazy('login'))
def event_adder(request):
    user = request.user
    user_data = Club_Company.objects.filter(user_id = user)[0]
    
    if request.method == 'POST':
        new_id = True
        while new_id:
            eid = random.randint(1111111111,9999999999)
            if len(EventData.objects.filter(event_id = eid)) == 0:
                new_id = False
                
        if request.POST.get('free_gl') == 'on':
            free_gl = True
        else:
            free_gl = False
            
        if request.POST.get('paid_gl') == 'on':
            paid_gl = True
        else:
            paid_gl = False
            
        event_date_temp = str(request.POST.get('event_date')).split('-')
        event_date = datetime.date(year=int(event_date_temp[0]),month=int(event_date_temp[1]),day=int(event_date_temp[2])).strftime("%d %B, %Y")
        
        event_time_temp = str(request.POST.get('event_time')).split(':')
        event_time = datetime.time(hour=int(event_time_temp[0]),minute=int(event_time_temp[1])).strftime("%I:%M %p")
        
        
        new_event = EventData(
            user_id = user,
            event_id = eid,
            event_name = request.POST.get('event_name'),
            event_desc = request.POST.get('event_desc'),
            event_venue = request.POST.get('event_venue'),
            event_date = event_date,
            event_time = event_time,
            event_date_alt = request.POST.get('event_date'),
            event_time_alt = request.POST.get('event_time'),
            host = request.POST.get('hosts'),
            collaborator = request.POST.get('collaborator'),
            free_gl = free_gl,
            paid_gl = paid_gl,
            pass_price = request.POST.get('pass_price'),
            gt_1 = request.POST.get('gt_1'),
            gt_2 = request.POST.get('gt_2'),
            gt_3 = request.POST.get('gt_3'),
            gt_4 = request.POST.get('gt_4'),
            gt_5 = request.POST.get('gt_5'),
            flyer = request.FILES.get('flyer'),
            table_chart = request.FILES.get('table_chart'),
        )
        new_event.save()
        return redirect('event',eid)

    data = {
        'user':user,
        'user_data':user_data,
        'logged_in':True,
    }
    return render(request,'event_adder.html',data)

@login_required(login_url=reverse_lazy('login'))
def event_edit(request,id):
    event_data = EventData.objects.filter(event_id=id)[0]
    user = request.user
    if str(event_data.user_id) != str(user):
        return redirect('dashboard')
    
    if request.method == 'POST':
        event_obg = EventData.objects.get(event_id=id)
        event_date_temp = str(request.POST.get('event_date')).split('-')
        event_date = datetime.date(year=int(event_date_temp[0]),month=int(event_date_temp[1]),day=int(event_date_temp[2])).strftime("%d %B, %Y")
        
        event_time_temp = str(request.POST.get('event_time')).split(':')
        event_time = datetime.time(hour=int(event_time_temp[0]),minute=int(event_time_temp[1])).strftime("%I:%M %p")
        
        event_obg.event_name = request.POST.get('event_name')
        event_obg.event_desc = request.POST.get('event_desc')
        event_obg.event_venue = request.POST.get('event_venue')
        event_obg.event_date = event_date
        event_obg.event_time = event_time
        event_obg.event_date_alt = request.POST.get('event_date')
        event_obg.event_time_alt = request.POST.get('event_time')
        event_obg.host = request.POST.get('hosts')
        event_obg.collaborator = request.POST.get('collaborator')
        event_obg.pass_price = request.POST.get('pass_price')
        event_obg.gt_1 = request.POST.get('gt_1')
        event_obg.gt_2 = request.POST.get('gt_2')
        event_obg.gt_3 = request.POST.get('gt_3')
        event_obg.gt_4 = request.POST.get('gt_4')
        event_obg.gt_5 = request.POST.get('gt_5')
        
        event_obg.save()
        return redirect('event',id)
        
    data={
        'event_data':event_data,
        'logged_in':True,
    }
    return render(request,'event_edit.html',data)

@login_required(login_url=reverse_lazy('login'))
def event_report(request,id):
    try:
        user = request.user
        event_data = EventData.objects.filter(event_id=id,user_id = user)[0]
        stag_data = Stag.objects.filter(event_id  = id)
        couple_data = Couple.objects.filter(event_id  = id)
        total_stag = 0
        total_couple = 0
        for stag_info in stag_data:
            total_stag += int(stag_info.pass_qty)    
        # for couple_info in couple_data:
        #     total_couple += int(couple_info.pass_qty)       

        
        data = {
            'event_data':event_data,
            'stag_data':stag_data,
            'total_stag':total_stag,
            'couple_data':couple_data,
            'total_couple':len(couple_data),        
            # 'total_couple':total_couple,
            'logged_in':True,
        }
        
        return render(request,'event_report.html',data)

    except:
        return redirect('home')

## ------ Pass Handler ------ ##
def generated_pass_stag(request,uid):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    user_data = Stag.objects.filter(user_id = uid)
    if len(user_data) > 0:
        user_data = user_data[0]
        event_id = user_data.event_id
        event_data = EventData.objects.filter(event_id=event_id)[0]
        
        data = {
            'user_data':user_data,
            'event_data':event_data,
            'logged_in':logged_in,
        }
        
        return render(request,'generated_pass_stag.html',data)
    
    else:
        return redirect('home')
    
def generated_pass_couple(request,uid):
    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False
    user_data = Couple.objects.filter(user_id = uid)
    if len(user_data) > 0:
        user_data = user_data[0]
        event_id = user_data.event_id
        event_data = EventData.objects.filter(event_id=event_id)[0]
        
        data = {
            'user_data':user_data,
            'event_data':event_data,
            'logged_in':logged_in,
        }
        
        return render(request,'generated_pass_couple.html',data)
    
    else:
        return redirect('home')

@login_required(login_url=reverse_lazy('login'))
def qr_check_stag(request,eid,uid):
    user = request.user
    event_data = EventData.objects.filter(event_id = eid, user_id = user)
    if len(event_data) > 0:
        try:
            user_obj = Stag.objects.get(user_id = uid, event_id = eid)
            if user_obj.entered == False:
                user_obj.entered = True
                user_obj.save()
                success = 1 #Allow User
            else:
                success = 2 # Already entered
        except:
            user_obj = None
            success = 3 # No user
    else:
        return redirect('home')
    
    data = {
        'event_data':event_data[0],
        'success':success,
        'user_data':user_obj,
        'type':'Stag',
    }
    
    return render(request,'qr_check.html',data)

@login_required(login_url=reverse_lazy('login'))
def qr_check_couple(request,eid,uid):
    user = request.user
    event_data = EventData.objects.filter(event_id = eid, user_id = user)
    if len(event_data) > 0:
        try:
            user_obj = Couple.objects.get(user_id = uid, event_id = eid)
            if user_obj.entered == False:
                user_obj.entered = True
                user_obj.save()
                success = 1 #Allow User
            else:
                success = 2 # Already entered
        except:
            user_obj = None
            success = 3 # No user
    else:
        return redirect('home')
    
    data = {
        'event_data':event_data[0],
        'success':success,
        'user_data':user_obj,
        'type':'Couple',
    }
    
    return render(request,'qr_check.html',data)        
 
## ------ Admin Side ------ ##
@login_required(login_url=reverse_lazy('login'))
def check_users(request):  
    if request.user.is_staff:
        user_data = Club_Company.objects.filter(activated = False)
        data = {
            'user_data':user_data,
        }
        return render(request,'check_users.html',data)
    else:
        return redirect('login')
 
@login_required(login_url=reverse_lazy('login'))
def user_activate(request,id):
    try:
        if request.user.is_staff:
            user_obg = Club_Company.objects.get(user_id=id)
            user_obg.activated = True
            user_obg.save()
            return HttpResponse(f'User Activated')
        else:
            return redirect('home')            
    except:
        return redirect('home')
 