from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.shortcuts import render, redirect
from django.views import View

from books.models import Book
from users.forms import CustomUserCreateForm, UserUpdateForm, UserLoginForm, UserCreateForm


# Create your views here.
class RegisterView(View):
    @staticmethod
    def get(request):
        create_form = CustomUserCreateForm()
        context = {
            'form': create_form,
        }
        return render(request,'users/register.html', context)

    @staticmethod
    def post(request):

        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form,
            }
            return render(request, 'users/register.html', context)




class LoginView(View):
    @staticmethod
    def get(request):
        login_form = UserLoginForm()

        return render(request,'users/login.html', {'login_form': login_form})

    def post(self,request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are logged in')

            return redirect('books:list')

        else:
            return render(request,'users/login.html', {'login_form': login_form})

class ProfileView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request,'users/profile.html', {'user':request.user})

class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('landing_page')

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self,request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request,'users/profile_edit.html', {'form': user_update_form})

    def post(self,request):
        user_update_form = UserUpdateForm(
            data=request.POST,
            instance=request.user,
            files=request.FILES,
        )

        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, 'You have been updated')
            return redirect('users:profile')

        return render(request,'users/profile_edit.html', {'form': user_update_form})

