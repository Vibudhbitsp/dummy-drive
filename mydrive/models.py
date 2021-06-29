from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to='media')
    title = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title
        
