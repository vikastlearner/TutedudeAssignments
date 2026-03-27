from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    country = models.CharField(max_length=50)
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): return self.userid


