from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .forms import taskForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def Hello(request):
    return HttpResponse("Welcome to the Internship Program")

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def Task_list(request):
    # tasks = Task.objects.all()
    # return render(request,'tasks/task_list.html',{'tasks':tasks})
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        tasks = Task.objects.all().order_by('-created_at')

    #tasks = Task.objects.all().order_by('-created_at') #display by latest task first
        #pagination
    paginator = Paginator(tasks,5) #show 5 task per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'tasks/task_list.html',context)

  
@login_required
def create_task(request):
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')    
    return render(request,'tasks/create_task.html',{'form':form})

@login_required
def task_detail(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    return render(request,'tasks/task_detail.html',{'task':task})

def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'tasks/delete_task.html',{'task':task})

def edit_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    form = taskForm(instance=task)
    if request.method == 'POST':
        form = taskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail',task_id=task.id)
    context= {'form':form,'task':task}
    return render(request,'tasks/edit_task.html',context)