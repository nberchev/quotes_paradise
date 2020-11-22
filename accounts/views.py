from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, RegisterForm, ProfileForm
from accounts.models import ProfileUser


def profile_details(request, pk):
    profile = ProfileUser.objects.get(user_id=pk)

    context = {
        'profile': profile,
    }

    return render(request, 'registration/profile.html', context)


def register_user(request):
    if request.method == 'GET':
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'registration/register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('all quotes')

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'registration/register.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }

        return render(request, 'registration/login.html', context)
    else:
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('all quotes')

        context = {
            'login_form': login_form,
        }

        return render(request, 'registration/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing')
