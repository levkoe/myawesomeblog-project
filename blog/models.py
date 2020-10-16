from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    post_title = models.CharField(max_length=200, unique=True)
    post_text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to="post_images/")
    post_status = models.IntegerField(choices=STATUS, default=0)

    def get_summary(self):
        return self.post_text[:144]

    def __str__(self):
        return self.post_title
