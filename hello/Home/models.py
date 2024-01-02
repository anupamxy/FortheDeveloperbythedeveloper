from django.db import models
from django.contrib.auth.models import User 
class GeeksModel(models.Model):
 
    # fields of the model
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length = 200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    desc2 = models.CharField(max_length=255, blank=True, null=True)  # Add the new field
    date = models.DateField()
def __str__(self):
    return self.name

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)

class MyModel(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
