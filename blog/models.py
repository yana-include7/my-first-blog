from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    profile_image =  models.ImageField(upload_to='img',default='img/9.png')

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


    def __str__(self):
        return self.title