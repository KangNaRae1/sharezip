from django.db import models

# Create your models here.
class Message(models.Model):
    time=models.DateTimeField('date published')
    body=models.TextField()
    sender=models.CharField(max_length=150)
    receiver=models.CharField(max_length=150)

    def __str__(self):
        return self.body