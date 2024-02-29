from django.db import models

# Create your models here.
# we can understand this as we created a xcel sheet named contact
class contact(models.Model):
    name = models.CharField(max_length=122,default='')
    email = models.CharField(max_length=122,default='')
    date = models.DateField()

    def __str__(self):
        return self.name

class loginDetails(models.Model):
    username = models.CharField(max_length=122,default='')
    password = models.CharField(max_length=122,default='')

    def __str__(self):
        return self.username