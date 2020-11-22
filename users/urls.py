"""User views"""

# Django
from django.urls import path


# views
from users import views

urlpatterns = [

    path(
        route='profile/<str:username>/',
        view=views.DetailUser.as_view(template_name='users/detail.html'),
        name='detail'
    ),
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup_view,
        name='signup'
    ),
    path(
        route='me/update_profile/',
        view=views.update_profile,
        name='update'
    )
]
