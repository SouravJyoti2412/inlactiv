from django.db import models
from django.utils.timezone import datetime
from datetime import timedelta


# class basemodel(models.Model):
#     date = models.CharField(max_length=2 , verbose_name="today")
#     month = models.CharField(max_length=2)
#     year = models.CharField(max_length=4)
    
    
    
class Customer_singup(models.Model):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Student'
        verbose_name_plural = 'Student List'
    
    number =models.CharField(max_length=15,null = True, blank = True,verbose_name="phone number")
    password =models.CharField(max_length=255)
    forgetpass = models.IntegerField(default = 0,null =True,blank = True)
    Customer_otp = models.CharField(max_length=4)
    is_otp_validate = models.BooleanField(default=False)
    Create_at = models.DateTimeField(auto_now_add=True)
    
    # @staticmethod
    # def get_singup_detail_byid(id):
    #     try:
    #         return Customer_singup.objects.filter(id=id)
    #     except:
    #         return False
    # @staticmethod
    # def gets_singup_detail_byid(id):
    #     try:
    #         return Customer_singup.objects.get(id=id)
    #     except:
    #         return False
            
    
    # @staticmethod
    # def email_exists(self) :
    #     if Customer_singup.objects.filter(email =self.email):
    #         return True
    #     return False
    
    # @staticmethod
    def get_customer_details_by_number(number):
        try:
            return Customer_singup.objects.get(number = number)
        except:
            return False

    def __str__(self):
        return  self.number    


# class Customer_otp(models.Model):
#     nowtime = datetime.now()
#     timer = datetime.now() + timedelta(minutes=3)
#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Customer Tokens'
#         verbose_name_plural = 'Customer Tokens'
#     username = models.OneToOneField(Customer_singup, on_delete = models.CASCADE)
#     genarate_otp = models.CharField(max_length = 100 , default = 12345)  # type: ignore
#     genarate_token = models.CharField(max_length = 500 , default = "nothing")
#     created_at = models.DateTimeField(null = True , blank = True)
#     valid_at = models.DateTimeField(null = True , blank = True )
#     active = models.BooleanField(default = True)


# class Customer_information(models.Model):
#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'Student information'
#         verbose_name_plural = 'Student informations'
#     Customer = models.ForeignKey(Customer_singup, on_delete = models.CASCADE)
#     name = models.CharField(max_length=50,verbose_name="Name")  
#     email=models.EmailField(verbose_name="Email Id", null = True)
#     School = models.CharField(max_length=100)
#     Street_adress = models.TextField()
#     city = models.CharField(max_length=50)
#     district = models.CharField(max_length=50)
#     State = models.CharField(max_length=100)
#     pincode = models.CharField(max_length=6)
#     landmark = models.CharField(max_length=50, blank = True, null=True )