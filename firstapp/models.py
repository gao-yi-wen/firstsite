from django.db import models

# Create your models here.
class People(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name

class Articles(models.Model):
    title=models.CharField(null=True,blank=True,max_length=200)
    content=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title