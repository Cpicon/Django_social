# Django models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Models
from posts.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display = ('id', 'user', 'title', 'photo')
    list_filter = ('created', 'modified')


class PostInline(admin.StackedInline):
    """Profile in_line for users"""
    model = Post
    can_delete = True
    verbose_name_plural = 'posts'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (PostInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
