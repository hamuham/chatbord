from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import ChatModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
    # ユーザー作成処理
    print(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
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

def detailfunc(request, pk):
    object = get_object_or_404(ChatModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
    # object = get_object_or_404(ChatModel, pk=pk) こちらの記述が一般的
    object = ChatModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')

def readfunc(request, pk):
    object = ChatModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')

class ChatCreate(CreateView):
    template_name = 'create.html'
    model = ChatModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('list')