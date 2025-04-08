from datetime import date
from django.db import models
from typing import Any
from django.db.models.base import Model as Model
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manage import UserManager
from django.db import models




class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    mobile_number=models.CharField(max_length=14)
    is_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    forget_password=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='pics')
    address=models.TextField()
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_log_time=models.DateTimeField(null=True,blank=True)
    objects = UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


# Create your models here.

class Destination(models.Model):
    
    img =models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()

    def __str__(self) :
        return self.name
    
class AddDoctor(models.Model):
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    dob=models.DateField()
    address=models.TextField()
    gender = models.CharField(max_length=15)
    degree = models.CharField(max_length=50)
    speciality = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,unique=True)
    fees = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='pics/doctor')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Slot(models.Model):
    
    slot_time = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    class Meta:
        db_table = 'slot'


class Appointment(models.Model):
    patientid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctorid = models.ForeignKey(AddDoctor, on_delete=models.CASCADE)
    slotid = models.ForeignKey(Slot, on_delete=models.CASCADE)
    date = models.DateField()
    status =  models.CharField(max_length=50)
    

    class Meta:
        db_table = 'appoinment'

class Chatbot(models.Model):
    doctorid = models.ForeignKey(AddDoctor, on_delete=models.CASCADE)
    patientid = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(auto_now=True)
    message = models.CharField(max_length=1000)
    sender = models.CharField(max_length=200)

    class Meta:
        db_table = 'chatbot'

class Complain(models.Model):
    patient_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    complain_message = models.CharField(max_length=200)

    class Meta:
        db_table = 'complain'

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    msg = models.CharField(max_length=100)

    class Meta:
        db_table = 'contactus'

class Doctor(models.Model):
    drname = models.CharField(max_length=20)

    class Meta:
        db_table = 'Doctor'

class DoctorSchedule(models.Model):
    
    doctorid = models.ForeignKey(AddDoctor, on_delete=models.CASCADE)
    slotid = models.ForeignKey(Slot, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'DoctorSchedule'

class Feedback(models.Model):
    
    p_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    rate = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = 'feedback'

class Patient(models.Model):
    
    image = models.ImageField(upload_to='pics/patient')
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=14)

    class Meta:
        db_table = 'patient'


class Payment(models.Model):
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    fees = models.IntegerField()
    status = models.BooleanField(default=False)
    razorpay_pay_order_id= models.CharField(max_length=100,null=True,blank=True)
    razorpay_pay_payment_id= models.CharField(max_length=100,null=True,blank=True)
    razorpay_pay_signature_id= models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        db_table = 'payment'


class ShowAppointment(models.Model):
    
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    date = models.DateField()
    prescription = models.CharField(max_length=1000)
    chat = models.CharField(max_length=1000)

    class Meta:
        db_table = 'showappointment'


class Speciality(models.Model):
    
    speciality = models.CharField(max_length=30)

    class Meta:
        db_table = 'speciality'