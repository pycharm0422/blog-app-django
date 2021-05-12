from django.contrib.auth.forms import forms, UserCreationForm
from .models import Posts, Profile, Comments
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BlogUpdateCreate(ModelForm):
    class Meta:
        model = Posts
        fields = ['author', 'public_view', 'title', 'content']

        # def form_valid(self, form):
        #     form.instance.author = self.request.user

class accountUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # exclude = ['user']

class accountCreate(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class createComment(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
            
