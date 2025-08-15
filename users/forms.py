from django import forms
from django.core.mail import send_mail

from users.models import CustomUser
from django.forms import ModelForm


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        # if user.email:
        #     send_mail(
        #         'Welcome to Goodreads',
        #         f'Hi {user.first_name} {user.last_name}!',
        #         'akmalusmonov446@gmail.com',
        #         [user.email],  # qabul qiluvchilar ro‘yxati bo‘lishi kerak
        #     )

        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','email', 'profile_picture')


class CustomUserCreateForm:
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']