from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def welcome(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        user = User.objects.get(pk=user_id)
        username = user.username
    else:
        username = ''
    return render(request, "website/welcome.html",
                  {"current_user": username})


def about(request):
    return HttpResponse("We are Mahnaz & Mazhar!")


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # response = HttpResponse("Login successful")
            # response.set_cookie('user_id', user.id)
            request.session['user_id'] = user.id
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'website/signin.html', {'form': form})


def signOut(request):
    logout(request)
    return redirect('signin')
