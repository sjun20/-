from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Parking(models.Model):

    title = models.CharField(max_length=200)

    text = models.TextField()



    def __str__(self):
        return self.title

class Reserve(models.Model):
    parking = models.ForeignKey('blog.parking', related_name='reserves',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())
    approved_reserve = models.BooleanField(default=False)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def approve(self):
        self.approved_reserve = True
        self.save()

    def __str__(self):
        return self.text
