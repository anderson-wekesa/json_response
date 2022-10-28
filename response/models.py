from django.db import models

# Create your models here.
class Me(models.Model):
    slackUsername = models.CharField(max_length = 40)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(max_length = 100)