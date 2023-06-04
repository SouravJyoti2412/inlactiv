from django.contrib import admin
from user.models import Customer_singup
@admin.register(Customer_singup)
class Customer_singupAdmin(admin.ModelAdmin):
    list_display = ('number', 'password', 'forgetpass', 'Customer_otp' ,'is_otp_validate' ,'Create_at')
