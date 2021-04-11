from django.contrib import admin
from app.models import *

# Register your models here.
class Task_Admin(admin.ModelAdmin):
    list_display = ['user','task_title','task_description','task_add_date','task_for_date','remark','task_status']
class Customer_Admin(admin.ModelAdmin):
    list_display = ['name','email','phone','address']
class Activity_Admin(admin.ModelAdmin):
    list_display = ['name','activity','activity_add_date','activity_for_date']

admin.site.register(Task,Task_Admin)
admin.site.register(Customer,Customer_Admin)
admin.site.register(Activity,Activity_Admin)

