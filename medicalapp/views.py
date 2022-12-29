from django.shortcuts import redirect, render
from medicalapp.forms import signupform,medicineform
from medicalapp.forms import loginform
from medicalapp.models import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth  import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from medicalapp.models import Medicine

# Create your views here.

@login_required(login_url='login')
def home(request):
     if 'p' in request.GET:
        p=request.GET['p']
        obj=Medicine.objects.filter(name__icontains=p)
        
     else:
      obj=Medicine.objects.all()
        


     return render(request,'home.html',{'data':obj})

def login(request):
     if request.user.is_authenticated:
        return redirect('home')
     else:
      if request.method=='POST':
       username= request.POST.get('username')
       password= request.POST.get('password')

       user=authenticate(request, username=username,password=password)


       if user is not None:
        auth_login(request,user)
        return redirect('home')        
       
       else:
        messages.info(request,'username or password is incorrect')
        
     return render(request,'login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')



def signup(request):
     if request.user.is_authenticated:
        return redirect('home')
     else:
        form=signupform()
        if request.method=='POST':
         form=signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account was created')
            return redirect('login')


        context={
        'form':form
    }
     return render(request,'signup.html',context)

@login_required(login_url='login')
def create(request):
      if request.method=='POST':
        form=medicineform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            return redirect('create')

      else:
         form=medicineform    
   
      context={
        'form':form
    }
      return render(request,'create.html',context) 


def update(request,id):
    obj=Medicine.objects.get(id=id)
    form=medicineform(instance=obj)
    if request.method=='POST':
        form=medicineform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={
        'form':form
    }
    return render(request,'update.html',context)

    
@login_required(login_url='login')
def delete(request,id):
    obj=Medicine.objects.get(id=id)
    obj.delete()
    return redirect('home')
    return render(request,'delete.html',{'data':obj})