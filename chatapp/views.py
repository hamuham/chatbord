from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

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