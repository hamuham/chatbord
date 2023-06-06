from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
    # ユーザー作成処理
    print(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, 'test@test.com', password)
    return render(request, 'singup.html', {'some':100})