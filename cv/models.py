from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class main(models.Model):
    
    profile_pic=models.ImageField(upload_to="pics")
    name=models.CharField(max_length=50)
    current_position=models.CharField(max_length=50)
    about=models.TextField(default=None)

class educations(models.Model):
    education_title=models.TextField(default=None)
    name=models.CharField(max_length=100)
    grade=models.CharField(max_length=50)
    visit=models.TextField(default=None)

class skills(models.Model):
    skill_title=models.TextField(default=None)
    
class certifications(models.Model):
    logo=models.ImageField(upload_to='pics',default='san.jpg')
    certification_title=models.TextField(default=None)
    issued_by=models.CharField(max_length=200)
    visit=models.CharField(max_length=500)

class achievements(models.Model):
    achievement=models.TextField(default=None)
    
class hobbies(models.Model):
    hobbie=models.TextField(default=None)

