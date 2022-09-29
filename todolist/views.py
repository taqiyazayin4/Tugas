from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from todolist.models import Task
from todolist.forms import Form
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist (request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'tasks' : data_todolist,
        'username': request.user.username,
    }

   
    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def creating_new_task(request):
    form_task = Form()

    if request.method == 'POST':
        form_task = Form(request.POST)
        form_task.instance.user = request.user
        if form_task.is_valid():
            form_task.save()
            
            return redirect('todolist:show_todolist')
    context = {'form': form_task}
    return render(request, 'creating_new_task.html', context)

@login_required(login_url='/todolist/login/')
def update_status(request,id):
    
    form_task = Task.objects.get(id=id)
    form_task.is_finished = not form_task.is_finished
    form_task.save()

    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def remove_task (request, id):
    Task.objects.filter(id=id).delete()
    return redirect('todolist:show_todolist')