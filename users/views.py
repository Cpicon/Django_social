from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

# models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True

from users.models import Profile
from users.forms import ProfileForms


# Create your views here.

@login_required
def update_profile(request):
    """ update a user's profile"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('feed')
    else:
        form = ProfileForms()

    return render(request, template_name='users/update_profile.html', context={
        'profile': profile,
        'user': request.user,
        'form': form
    })


def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


def singup_view(request):
    """Sign up a user"""
    print(request.data)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        if password != password_confirm:
            return render(request, 'users/signup.html', {'error': ' Password confirmation does not match'})
        else:
            try:
                user = User.objects.create_user(username, password)
            except IntegrityError:
                return render(request, 'users/signup.html', {'error': 'Username already exists'})
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name ']
            user.email = request.POST['email']
            profile = Profile.objects.create(user)
            profile.save()
            user.save()
        return redirect('login')
    return render(request, 'users/signup.html')


