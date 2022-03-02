from django.db import models

# Create your models here.

# Work Model
class Works(models.Model):
    workId = models.AutoField(primary_key=True)
    img_string = models.TextField()
    title = models.CharField(max_length=300)
    tag = models.CharField(max_length=200)
    poper = models.CharField(max_length=200)
    project_link = models.CharField(max_length=300)
    description = models.TextField()
    
# Testimonials Model
class Testimonials(models.Model):
    testimonialId = models.AutoField(primary_key=True)
    img_string = models.TextField()
    Full_Name = models.CharField(max_length=200)
    Job_Title = models.CharField(max_length=200)
    Comments = models.TextField()

# profilepic
class Profilpic(models.Model):
    pro_count = models.AutoField(primary_key=True)
    img_string = models.TextField()