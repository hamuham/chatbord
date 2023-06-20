from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import ChatModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def signupfunc(request):
    # ユーザー作成処理
    print(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, password)
        except IntegrityError:
            return render(request, 'singup.html', {'error':'このユーザーは登録されています'})


    return render(request, 'singup.html', {'some':100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'context':'ログインできなかった'})

    return render(request, 'login.html')

@login_required
def listfunc(request):
    object_list = ChatModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')
