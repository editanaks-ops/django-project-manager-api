from django.shortcuts import render, redirect
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save()

            user.profile.role = form.cleaned_data['role']
            user.profile.save()

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def is_admin(user):
    return user.is_authenticated and user.profile.role == 'admin'


def is_manager(user):
    return user.is_authenticated and user.profile.role == 'manager'


def is_regular_user(user):
    return user.is_authenticated and user.profile.role == 'user'