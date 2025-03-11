from django.db import models

# Create your models here.

class Trainee(models.Model):
    trainee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    img = models.ImageField(upload_to='trainee/image')
    isactive = models.BooleanField(default=True)
