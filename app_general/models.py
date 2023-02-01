from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Contact(models.Model):
    company = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    cusemail = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.cusemail
    
class Video(models.Model):
    title = models.CharField(max_length=140)
    added = models.DateTimeField(auto_now_add=True)
    url= EmbedVideoField(max_length=140, blank=True, null=True)

    def __str__(self) :
        return str(self.title)
    
    class Meta:
        ordering = ['-added']

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=255)
    course_days = models.CharField(max_length=10)
    course_fee = models.CharField(max_length=50)
    course_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.course_name