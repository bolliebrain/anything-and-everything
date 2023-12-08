from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    dateposted = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    datecommented = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.comment