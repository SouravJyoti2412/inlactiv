from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.helpers import send_otp_ro_phone
from user.models import Customer_singup
from django.contrib.auth.hashers import make_password , check_password
def login_view(request):
    return render(request ,"user/login.html" )
def signup_view(request):
    return render(request , "user/signup.html")
def otp_view(request):
    return render(request ,"user/get-otp.html")

@api_view(["POST"])
def send_otp(request):
    data = request.data
    if  data.get("phone_number") is None:
        return Response({
            'status':400 , 
            "messege":"Phone number is required"
        })
    if  data.get("password") is None:
        return Response({
            'status':400 , 
            "messege":"password is required"
        })
        
    user = Customer_singup.objects.create(
        number = data.get("phone_number"),
        Customer_otp = send_otp_ro_phone(data.get("phone_number"))
        
    )
    user.password = make_password(data.get("password"))
    user.save()
    customer = Customer_singup.get_customer_details_by_number(data.get("phone_number"))
    request.session["customer_number"]= customer.number
    return Response({
        'status':200.,
        "messege":"otp Send successfully"
    })
    
    
    
    
@api_view(["POST"])
def verify_otp(request):
    data = request.data
    if  data.get("phone_number") is None:
        return Response({
            'status':400 , 
            "messege":"Phone number is required"
        })
    if  data.get("otp") is None:
        return Response({
            'status':400 , 
            "messege":"password is required"
        })
    try :
        user = Customer_singup.objects.get(number = data.get("phone_number"))
    except Exception as e:
        return Response({
                'status':400,
                "messege":"Invalid Phone number"
            })

    if user.Customer_otp == data.get("otp"):
        user.is_otp_validate = True
        user.save()
        return Response({
                'status':200,
                "messege":"otp matched"
            })
    else:
        return Response({
                'status':400,
                "messege":"otp not matched"
            })