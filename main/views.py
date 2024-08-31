from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, add_record, next_record

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from . models import Record

def webapp(request):
    return render(request, 'main/index.html')


# -- Register View

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("my-login")  # Use a URL name or path to redirect to the login page

    context = {'form': form}
    return render(request, 'main/register.html', context=context)  # Use render to display the template


# -- Login View

def my_login(request):
    form = LoginForm()

    if request.method =="POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)

                return redirect("dashboard")
    
    context = {'form':form}
    return render(request, 'main/my-login.html', context=context)


# --Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'recodrs':my_records}
    return render(request, 'main/dashboard.html', context=context) 



# --user logut
def user_logout(request):

    auth.logout(request)

    return redirect("my-login")


# -- RECORD CREATION

@login_required(login_url='my-login')
def create_record(request):
    form = add_record

    if request.method =="POST":
        form = add_record(request.POST)

        if form.is_valid():
            form.save()

            return redirect("dashboard")
        
    context = {'form':form}
    return render(request, 'main/create-record.html', context=context)


# -- Update the record
@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = next_record(instance=record)
    if request.method =="POST":
        form = next_record(request.POST, instance=record)

        if form.is_valid():
            form.save()

            return redirect("dashboard")
        
    context = {'form':form}
    return render(request, 'main/update-record.html', context=context)


# -- Read/view the singular record
@login_required(login_url='my-login')
def view_record(request, pk):
    
    all_records = Record.objects.get(id=pk)
    context = {'record':all_records}

    return render(request, 'main/view-record.html', context=context)


#-- create a delete function
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()

    return redirect("dashboard")