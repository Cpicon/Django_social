"""User's views"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse

# models
from django.contrib.auth.models import User
from users.forms import ProfileForms, SignupForm
from posts.models import Post

#settings
User._meta.get_field('email')._unique = True


# class views

class DetailUser(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        """Add posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


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

            url = reverse('users:update', kwargs={
                'username': request.user.username
            })
            return redirect(url)
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
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('users:login')


def signup_view(request):
    """Sign up a user"""

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(
        request,
        template_name='users/signup.html',
        context={
            'form': form
        }
    )
