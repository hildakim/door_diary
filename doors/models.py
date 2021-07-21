from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class PhotoDiary(models.Model):
    body = models.TextField()
    upload_date = models.DateTimeField()
    image = models.ImageField(upload_to='doors/', null=False, blank=False,  default='default-image.jpg')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 150)])
   

def __str__(self):
    return self.title 

def summary(self):
    return self.body[:100]