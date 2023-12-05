from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    dateposted = models.DateField()

    def __str__(self):
        return self.title

