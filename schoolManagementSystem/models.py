from ast import mod
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    date_of_birth =models.DateField()
    county = models.CharField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    Nationality = models.CharField()
    date_of_enrollment = models.DateField()
    laptop_serial_number = models.CharField()
    health_status = models.FileField()
    Phone_number = models.CharField(max_length=15)
    languages = models.CharField()
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)
    CLASS_CHOICES = (
        ('A', 'Ada'),
        ('A', 'AnitaB'),
        ('H','Hopper',)
    )
    classes = models.CharField(max_length=1,choices=CLASS_CHOICES,null=True)
    National_Id = models.CharField(max_length=15)

 

class Trainer(models.Model):
        trainer_name = models.CharField(max_length=50)
        Trainer_name_name = models.CharField(max_length=50)
        surname_name = models.CharField(max_length=50)

        GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )

        trainer_gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)

        COURSE_CHOICES = (
        ('J', 'JavaScript'),
        ('K', 'Kotlin'),
        ('P','Python'),
        ('R','Research'),
        ('D','Design'),
        ('I','IoT'),
    )
        course = models.CharField(max_length=1,choices=COURSE_CHOICES,null=True)
        age = models.SmallIntegerField()
        Email_address = models.EmailField()
        pho_number = models.CharField(max_length=15)
        salary = models.PositiveBigIntegerField()
        Profile_pic= models.ImageField(upload_to='profile_pictures/',null=True)
        dateHired = models.DateField()











        
















 



