from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=60,null=True)
    message=models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name

    

