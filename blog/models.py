from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    body=models.TextField()
    image=models.ImageField()
#title
#pub_date
#body
#image
