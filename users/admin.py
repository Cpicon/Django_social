"""User admin clases"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Profile admin'''
    list_display = ('pk', 'user', 'website', 'phone_number', 'picture')
    list_display_links = ('pk', 'user', 'website')
    list_editable = ('phone_number', 'picture')
    search_fields = (
        'user__first_name',
        'user__last_name',
        'user__email',
        'phone_number'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'modified',
        'created'
    )
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                'biography'
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )
    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in_line for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)