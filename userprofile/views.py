from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from team.models import Team
from userprofile.models import Userprofile


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # userprofile = Userprofile.objects.create(user=user)
            Userprofile.objects.create(user=user)
            team = Team.objects.create(name='The team name', created_by=request.user)
            team.members.add(request.user)
            team.save()
            return redirect('userprofile:login')
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/sign_up.html', {
        'form': form
    })


def sign_in(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('core:index')
    else:
        form = AuthenticationForm()
    return render(request, 'userprofile/login.html', {
        'form': form
    })


def sign_out(request):
    logout(request)
    return redirect('userprofile:sign_in')


@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request, 'userprofile/myaccount.html', {
        'team': team,
    })
