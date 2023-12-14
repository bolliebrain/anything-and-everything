from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    slug = models.SlugField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="aande_posts", null=True)
    description = models.CharField(max_length=100, null=False, blank=False)
    dateposted = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commentpost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="aande_comments", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user", null=True)
    comment = models.CharField(max_length=200, null=False, blank=False)
    datecommented = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Comment {self.comment} by {self.user} on {self.datecommented}"