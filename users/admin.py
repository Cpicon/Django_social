"""User admin clases"""

#Django
from django.contrib import admin
#Models

from users.models import Profile
# Register your models here.

@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    '''Profile admin'''
    list_display = ('pk', 'user', 'website', 'phone_number', 'picture')
    list_display_links = ('pk', 'user', 'website')
    list_editable = ('phone_number','picture')
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
    fieldsets = (('Profile',
                 {
                     'fields': (('user', 'picture'),
                                ('website','phone_number')),
                 }),
    )