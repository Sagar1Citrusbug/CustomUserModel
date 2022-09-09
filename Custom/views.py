from http.client import HTTPResponse


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import myUser

from .forms import Register 
def thanks(request):
    return render(request, "Custom/thanks.html")
def home(request):
    print("uksersjflksdjflkjflkfjsdlkfjslkdfj")
    context  ={}
    users = myUser.objects.all()
    
        
    context['allUsers'] = users
    return render(request, "Custom/all_users.html", context)

def registration_view(request):
    context = {}
    if request.method == 'POST':
        
        form = Register(request.POST)
        print(form.errors)
        if form.is_valid():
           
            print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
            form.save()
            email =  form.cleaned_data.get('email')
            # name   = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
            
            account = authenticate(email = email, password = password)
            login(request, account)
            return redirect("thanks")
        else:
            print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
            context['form'] = form
            return render(request, "Custom/register.html", context)
    else:
        print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
        form= Register()
        context['form'] = form
        return render(request, "Custom/register.html", context)