from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from .models import Registration
import random

def generate_otp():
    return str(random.randint(1000, 9999))

def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        gender=request.POST['gender']
        sclass=request.POST['sclass']
        phn=request.POST['phn']
        admin=int(request.POST['admin'])
        if admin>65:
            otp = generate_otp()
            subject=f"Welcome {name}"
            to=email
            from_email=  'mdabuoff@gmail.com'
            message =f"You have successfully registered in the student registration form!  Your registration OTP is {otp}"
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    [to],
                )
                dt=Registration(Name=name,Email=email,Dob=dob,Gender=gender,Sclass=sclass,PhnNum=phn,AdminScore=admin,Otp=otp)
                dt.save()
                print(name,email,dob,gender,sclass,phn,admin,otp)
                return render(request,'reg.html', {'email': email})
            except Exception:
                    return HttpResponse("Admin score must be greater than 65.")
        else:
            subject=f"Welcome {name}"
            to=email
            from_email=  'mdabuoff@gmail.com'
            message = "Your Admission test score is low !"
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    [to],
                )
                print(name,email,dob,gender,sclass,phn,admin)
                return render(request,'index.html')
            except Exception:
                    return HttpResponse("Admin score must be greater than 65.")
    else:
        return render(request,'index.html')

def list(request):
    dt=Registration.objects.all()
    return render(request,'lists.html',{'dt':dt})

def verify(request):
    if request.method == "POST":
        entered_otp = request.POST.get('code')
        email = request.POST['email']
        registrations = Registration.objects.filter(Email=email)
        if registrations.exists():
            stored_otp = registrations.first().Otp
            print(f"Entered OTP: {entered_otp}, Stored OTP: {stored_otp}")
            if entered_otp == stored_otp:
                print("OTP Matched - Rendering lists.html")
                return render(request, 'sucess.html')
            else:
                print("OTP Mismatch - Rendering reg.html")
                return render(request, 'reg.html',{'email': email})
        else:
            print("User not found - Rendering index.html")
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


