from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import *


class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class Task_update_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['remark','task_status']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
class ActivityForm(forms.ModelForm):
    class Meta:
        model=Activity
        fields='__all__'
#
# class Payment_detailForm(forms.ModelForm):
#     class Meta:
#         model = Payment_detail
#         fields= ['payment_screenshot']


