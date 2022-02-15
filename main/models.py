from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField() #글 등록할 때 timezone으로부터 받아옴
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class campinfo(models.Model):
    text = models.CharField(max_length=255, null = False)