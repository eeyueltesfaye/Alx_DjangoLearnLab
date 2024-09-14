from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import Post, Tag
from .models import Comment

  #user registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

  # user profile update form 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required = False
    )
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']