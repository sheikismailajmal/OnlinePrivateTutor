from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=20)
    viewPassword=models.CharField(max_length=200,null=True)

class Parent(models.Model):
    parent= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20)
    Address=models.CharField(max_length=200)
    status=models.CharField(max_length=20,default='pending')

class Student(models.Model):
    student= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username2=models.CharField(max_length=20)
    Email2=models.EmailField()
    Phonenumber2=models.IntegerField()
    Password2=models.CharField(max_length=20)
    Address2=models.CharField(max_length=200)

class Teacher3(models.Model):
    teacher= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    username5=models.CharField(max_length=20)
    email5=models.EmailField()
    image5=models.ImageField(upload_to="image",null=True)
    password5=models.CharField(max_length=20)
    subject5 = models.CharField(max_length=200)
    location5 = models.CharField(max_length=100)
    status=models.CharField(max_length=20,default='pending')
    fee = models.IntegerField(null=True)
    reviews_count = models.IntegerField(default=0,null=True)
    average_rating=models.IntegerField(default=0,null=True)

class Book(models.Model):
    Bookname=models.CharField(max_length=20)
    Image=models.ImageField(upload_to="image",null=True)
    Description=models.CharField(max_length=200,null=True)
    subject1 = models.CharField(max_length=200,default="pending")
    link=models.CharField(max_length=400,null=True)

class Booking1(models.Model):
    parent= models.ForeignKey(Parent,on_delete=models.CASCADE,null=True)
    booking_type1 = models.CharField(max_length=10) 
    booking_time1= models.CharField(max_length=100)
    booked_datetime = models.DateTimeField(auto_now_add=True)
    teacher=models.ForeignKey(Teacher3,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')

class Requestdemo(models.Model):
    booking= models.ForeignKey(Booking1,on_delete=models.CASCADE,null=True)
    Video=models.FileField(upload_to='videos',null=True)
    date=models.DateField(auto_now_add=True,null=True)
    teacher=models.ForeignKey(Teacher3,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=20,default='pending')

class Message(models.Model):
    sender = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
    senderemail = models.CharField(max_length=300, null=True, blank=True)
    reciveremail = models.CharField(max_length=300, null=True, blank=True)
    receiver = models.ForeignKey(Teacher3, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=300, null=True, blank=True)
    time = models.CharField(max_length=300, null=True)
    type = models.CharField(max_length=300, null=True)
    message = models.CharField(max_length=300, null=True)

class Review(models.Model):
    review=models.CharField(max_length=200,null=True)
    rating = models.IntegerField(default=0)
    teacher=models.ForeignKey(Teacher3,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    parent= models.ForeignKey(Parent,on_delete=models.CASCADE,null=True)

class Payment(models.Model):
    status=models.CharField(max_length=20,default='pending')
    parent= models.ForeignKey(Parent,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    teacher=models.ForeignKey(Teacher3,on_delete=models.CASCADE,null=True)
