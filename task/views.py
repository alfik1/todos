from django.shortcuts import render
from django.views.generic import View
from task.models import Task
# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"registration.html")

class AddTaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"task.html")
    
    def post(self,request,*args,**kwargs):
        user=request.POST.get("username")
        task=request.POST.get("task")
        Task.objects.create(task_name=task,user=user)
        return render(request,"task.html")

class TaskListView(View):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        return render(request,"tasklist.html",{"tasks":qs})
