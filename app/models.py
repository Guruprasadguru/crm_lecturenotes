from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (('Pending', 'Pending'), ('completed', 'completed'))
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    task_title=models.CharField(max_length=100)
    task_description=models.TextField(max_length=200)
    task_add_date=models.DateField(auto_now=True)
    task_for_date=models.DateField()
    remark=models.CharField(max_length=100,default=None)
    task_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Activity(models.Model):
    name=models.ForeignKey(Customer,null=True, blank=True, on_delete=models.CASCADE)
    activity=models.TextField(max_length=300)
    activity_add_date=models.DateField(auto_now=True)
    activity_for_date=models.DateField()


