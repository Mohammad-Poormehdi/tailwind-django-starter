from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class WorkExample(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="files")
    url = models.URLField()
    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number =  PhoneNumberField()
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    def __str__(self):
        return f'name:{self.name} project:{self.project_name}'