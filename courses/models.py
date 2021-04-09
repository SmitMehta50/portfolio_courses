from django.db import models

# Create your models here.

 
class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    name = models.CharField(max_length=20, default='Unknown')

    

    def __str__(self):
        return self.summary

