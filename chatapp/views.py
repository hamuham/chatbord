from django.shortcuts import render

# Create your views here.

def signupfunc(request):
    return render(request, 'singup.html', {'some':100})