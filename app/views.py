
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import sys,datetime
from app.models import *
from django.views.generic import ListView
from django.db.models import Q
import app
from app.forms import *
from app.models import *

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = Signup_form()

        if request.method == 'POST':
            form = Signup_form(request.POST)
            if form.is_valid():
                user = form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'app/signup.html', context)


# Create your views here.
@login_required
def home(request):
    task = Task.objects.filter(task_for_date=datetime.date.today())
    context = {'task': task}
    return render(request, 'app/home.html', context)
def task_update(request,id):
    if request.user.is_authenticated:
        user = request.user
        emp = Task.objects.get(user=user, id=id)
        form = Task_update_form(instance=emp)

        if request.method == 'POST':
            form =Task_update_form(request.POST, instance=emp)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request, 'app/task_update.html', {'form': form})

class Customer_list(ListView):
    model = Customer
    template_name = 'app/Customer_list.html'
    def get_queryset(self):
        customer_list =Customer.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            customer_list =Customer.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
        return customer_list
@login_required()
def activity(request,id):
    if request.user.is_authenticated:
        user = request.user
        pactivity=Activity.objects.filter(name_id__exact=id,activity_for_date__lte=datetime.date.today())
        factivity=Activity.objects.filter(name_id__exact=id,activity_for_date__gte=datetime.date.today())

        context = {'pactivity': pactivity,'factivity': factivity}
        return render(request, 'app/customer_activity.html',context)
@login_required()
def addcustomer(request):
    form=CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    return render(request, 'app/customerupdate.html', {'form': form})
@login_required()
def addactivity(request):
    form=ActivityForm()
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
    return render(request, 'app/addactivity.html', {'form': form})

@login_required
def myprofile(request):
    if request.user.is_authenticated:
        username = request.user.username
    context = {'username': username}
    return render(request, 'app/myprofile.html', context)