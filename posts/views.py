# Create your views here.

#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Models
from posts.models import Post

#Forms
from posts.forms import PostForm

@login_required
def list_posts(request):
    """return existing posts"""
    posts = Post.objects.all().order_by('-created')
    return render(request,
                  'posts/feed.html',
                  context={
                      'posts': posts,
                      'profile': request.user.profile
                  }
                  )

@login_required
def new_post(request):
    """Create new post view"""

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(
        request,
        'posts/new_post.html',
        context={
            'profile': request.user.profile,
            'form': form,
            'user': request.user
        }
    )