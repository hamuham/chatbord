from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import ChatModel

# Create your views here.

def signupfunc(request):
    # ユーザー作成処理
    print(request)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, 'singup.html', {'error':'このユーザーは登録されています'})


    return render(request, 'singup.html', {'some':100})

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, email=email, password=password)
        if user is not None:
            logint(request, user)
            return render(request, 'login.html', {'context':'ログインできた'})

        else:
            return render(request, 'login.html', {'context':'ログインできなかった'})

def listfunc(request):
    object_list = ChatModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})