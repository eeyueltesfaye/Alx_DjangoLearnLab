from django.shortcuts import render, redirect 
from .models import Post 
from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .forms import UserRegisterForm, UserUpdateForm 
from django.contrib import messages

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        
    return render(request, 'blog/register.html', {'form': form})
    
@login_required
def profile(request):
    if request.method == 'POST':
         u_form = UserUpdateForm(request.POST, instance=request.user)
         if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    
    context = {
        'u_form': u_form
    }
    return render(request, 'blog/profile.html', context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts':posts})
