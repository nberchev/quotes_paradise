from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/quotes/'


def redirect_user(request):
    url = f'/quotes/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
    pass
