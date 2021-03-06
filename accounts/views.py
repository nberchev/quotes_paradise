from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.forms import LoginForm, RegisterForm, ProfileForm, EditUserForm, EditProfileForm
from accounts.models import ProfileUser


@login_required
def profile_details(request, pk):
    profile = ProfileUser.objects.get(user_id=pk)

    context = {
        'profile': profile,
    }

    return render(request, 'registration/profile.html', context)


def register_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('all quotes')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'registration/register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

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
        if request.user.is_authenticated:
            return redirect('all quotes')

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

        messages.error(request, 'Incorrect username and/or password')
        return render(request, 'registration/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = EditUserForm(request.POST, instance=request.user)
        p_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profileuser)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile = request.user.profileuser
            p_form.user = profile
            p_form.save()
            return redirect('user profile', pk=request.user.pk)
    else:
        u_form = EditUserForm(instance=request.user)
        p_form = EditProfileForm(instance=request.user.profileuser)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'registration/edit_profile.html', context)
