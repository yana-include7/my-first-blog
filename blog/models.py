from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
import os
import logging
logger = logging.getLogger("mylogger")

mouth={"January":"январь",
"February":"февраль",
"March"	:"март",
"April"	:"апрель",
"May":"май",
"June":"июнь",
"July":"июль",
"August":"вгуст",
"September"	:"сентябрь",
"October":"октябрь",
"November":"ноябрь",
"December":"декабрь"}


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def _get_date(self):
        return  mouth.setdefault(self.created_date.strftime('%B'))+" "+self.created_date.strftime('%Y')
    date1 = property(_get_date)

    def _get_date2(self):
        logger.info(self.published_date)
        if self.published_date!=None:
            return  mouth.setdefault(self.published_date.strftime('%B'))+" "+self.published_date.strftime('%Y')
        else:return " "
    date2 = property(_get_date2)


class Photo(models.Model):
    title = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    profile_image= models.ImageField(upload_to='img', default='img/9.png')
    text = models.TextField(default='Здесь я')




