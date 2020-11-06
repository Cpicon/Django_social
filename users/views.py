from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

#models
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
from users.models import Profile

# Create your views here.


def login_view(request):
    """Login view"""
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
    else:
        return render(request, 'users/login.html', {'error':  'Invalid username or password'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')

def singup_view(request):
    """Sign up a user"""
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        if password != password_confirm:
            return render(request, 'users/singup.html', {'error': ' Password confirmation does not match'})
        else:
            try:
                user = User.objects.create_user(username, password)
            except IntegrityError:
                return render(request, 'users/singup.html', {'error': 'Username already exists'})
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name ']
            user.email = request.POST['email']
            profile = Profile.objects.create(user)
            profile.save()
            user.save()
        return redirect('login')
    return render(request, 'users/signup.html')