from django.db import models
from django.contrib.auth.models import User


class Login(models.Model):
    username=models.CharField(max_length=20)
    
    password=models.CharField(max_length=15)
    
# class Register(models.Model):
#     first_name=models.CharField(max_length=20)
#     last_name=models.CharField(max_length=20)
#     email=models.EmailField(max_length=20)
#     username=models.CharField(max_length=20)
#     password=models.CharField(max_length=15)
#     repassword=models.CharField(max_length=15)
#     phone_number=models.CharField(max_length=20)
    
class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=15)
    repassword=models.CharField(max_length=15)
    # phone_number=models.CharField(max_length=20)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    destination = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    arrival_date = models.DateField()
    leaving_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"{self.destination} ({self.arrival_date} to {self.leaving_date})"
   
class SlotReservation(models.Model):
    destination = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    number_of_members = models.CharField(max_length=50, choices=[
        ('2 to 4', '2 to 4'),
        ('4 to 6', '4 to 6'),
        ('6 to 10', '6 to 10'),
    ])
    arrival_date = models.DateField()
    leaving_date = models.DateField()
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.destination}"  