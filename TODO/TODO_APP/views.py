from django.shortcuts import render, redirect 
from django.contrib.auth.models import User, auth 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import TODO
from django.views.generic import UpdateView
import datetime


# Create your views here.
@login_required(login_url="login/")
def home(request):
    user = request.user
    log_time = datetime.datetime.today()
    # print(user,"    .   ./  .       /   .   /   .   /   .   /.      .   /   ./  .   /   .   /   .   ")
    lst = TODO.objects.filter(user = user)
    if request.POST:
        task = request.POST['task']
        # print("Task ",task ,    '   .   ..  .   .   .   Task    /   /   //  /   /   //      /   /   /   /   /   /   ')
        if task == " " or task == '  ':
            # print("Satisfy")
            return render(request , "index.html" , {'msg':"Please enter task" , "lst":lst})
        else:
            task = TODO.objects.create(todo_name = task , user = user)
            task.save()
            return redirect('home')
    return render(request, 'index.html' , {'lst':lst , "user":user , "log_time":log_time})



def logout_user(request):
    logout(request)
    return redirect('login')


def login_user(request):
    if request.POST:
        name = request.POST['username']
        password = request.POST['password']

        
        user = auth.authenticate(username = name , password = password)
        someone = User.objects.filter(username = name).exists()
        
        print(someone, "name of login")
         
        if not(someone):
            return render(request , "login.html " , {'msg':"Email is incorrect"})
        

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request , "login.html" , {'msg':"password is incorrect"})
    return render(request, 'login.html')



def signup_user(request):
    if request.POST:
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        chreck = User.objects.filter(username = email)

        if chreck:
            return render(request , "signup.html" , {'msg':'Email alredy Exist'})
        else:
            new_user = User.objects.create_user(first_name = firstname, last_name= lastname, username=email, password = password)
            new_user.save()
        
            return redirect('login')

    return render(request, 'signup.html')

def edit(request,id):
    change = TODO.objects.get(id=id)
    print(change,'  /   /   /   /   Id/   /   /   /   /   /   /   /   /')
    if change.status == True:
        print(change.status , " /   //  /   /   /   /   / Status  /   /   /   /   /   /   /   /")
        if request.POST:
            taskName = request.POST['newtask']
            print(taskName, 'Request.POST /   /   /   /   /   /   /')
            change.todo_name = taskName
            change.status = False
            change.save()
            return redirect('home')
        return render(request , "edit.html", {"change":change})
    else:
        change.status = True
        change.save()
        print(change.status)
        return render (request , 'edit.html', {"change":change})


# def update_name(request,id):
#     # print(taskId)
#     # print(taskId , "  .   .   .   .   ..  .   .   .   .   .   .       .   .")
#     change = TODO.objects.get(id=id)
#     print(change,'Satisfy  /   /   //  /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /')
#     if request.POST:
#         print('request.POST     /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /   /')
#         taskId = TODO.objects.get(id = id)
#         taskName = request.POST['newtask']
#         print(taskName)
#         change.todo_name = taskName
#         change.status = False
#         change.save()
#         # return redirect('home')
#         # return render(request , "edit.html" , {"change":change})
#     return render(request , "edit.html" , {"change":change})

def cancel(request , id):
    change = TODO.objects.get(id=id)
    if change.status == True:
        change.status = False
        change.save()
        return redirect('home')
    

def delete_task(request , id):
    remove = TODO.objects.get(id = id) 
    remove.delete()
    return redirect('home')











