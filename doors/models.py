from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class PhotoDiary(models.Model):
    upload_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='board/', null=True, blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(100, 100)])


def __str__(self):
    return self.title 

def summary(self):
    return self.body[:100]