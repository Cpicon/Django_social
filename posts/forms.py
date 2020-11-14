"""Post forms"""


#Django
from django import forms

#models
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta :
        """Form settings"""

        model = Post

        fields = ('user', 'profile', 'title', 'photo')

