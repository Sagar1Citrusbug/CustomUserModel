from django.http import HttpResponse


from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .models import myUser
from django.contrib.auth.models import User

from .forms import Register, LogPage, passwordchangeform
def thanks(request):
    return render(request, "Custom/thanks.html")
def home(request):
   
    context  ={}
    # users = myUser.objects.all()
    
        
    # context['allUsers'] = users
    return render(request, "Custom/all_users.html", context)




def registration_view(request):
    context = {}
    if request.method == 'POST':
        
        form = Register(request.POST)
        print(form.errors)
        if form.is_valid():
           
            
            form.save()
            
            email =  form.cleaned_data.get('email')
            name   = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
            # myUser.objects.create(name = name, email = email, password = password)
            # account = authenticate(email = email, password = password)
            # login(request, account)
            # print(request.user, "--------------------current User=----------------------------------")

            return redirect("thanks")
        else:
           
            context['form'] = form
            return render(request, "Custom/register.html", context)

    else:
       
        form= Register()
        context['form'] = form
        return render(request, "Custom/register.html", context)

def log_in(request):
   
    context= {}
    if request.method  == 'POST':
        print("------------------2------------")
        
        form = LogPage(request.POST)
        context['form'] = form
        print(form.errors)
        if form.is_valid():
            print("-------------3-------------------")
            email =  form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = myUser.objects.filter(email = email).first()
           
            if user:

                print(user, "---------------------")
                account = authenticate(email = email, password = password)
                print(account,"/////")
                if account:
                    login(request, user)

                    return render(request,"Custom/logout.html", {'user':user})
                else:
                    return HttpResponse("password or email is wrong")
            else:
                return  HttpResponse("NO user exists")
           
        else:
           
            return render(request, "Custom/login.html",{'form':form} )
    else:
        form = LogPage()
        context['form']  = form
        return render(request,"Custom/login.html")





def logout(request):

    print(request.user, "-------------------current user in session --------------------------------------")
def changepassword(request):
    if request.method == 'POST':
        form = passwordchangeform(request.POST)
        print("------------------------------cp111------------------------------")
        print(form.errors)
        if form.is_valid():
            print("---------------------cp222---------------")
            new_password = form.cleaned_data.get('new_password')
            old_password = form.cleaned_data.get('old_password')
            user = request.user
            if old_password == user.password:
                print("-------------------cp33333-----------------------------")
                user.set_password(new_password)
                user.save()
            
                return HttpResponse("Password changed")
            else:
                print("--------------------cp4444------------------------------")
                return HttpResponse("you have entered wrong password")
    else:

        form = passwordchangeform()
        return render(request,"Custom/passwordchange.html",{'form':form})


def logged(request):
    logout(request)
    print(request.user,"-----------------------------rajima ----------------------------lakhubha--------------------")
    return render(request,"Custom/loggedout.html")
    