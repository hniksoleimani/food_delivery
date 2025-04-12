from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from .models import Item
# from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, you have successfully logged in.')
            return redirect('login')
    else:
        form = RegisterForm()
    
        # form = UserCreationForm()
        
    
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profilepage(request):
    return render(request,'users/profile.html')

