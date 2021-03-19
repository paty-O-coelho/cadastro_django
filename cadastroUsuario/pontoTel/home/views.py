from django.shortcuts import redirect, render
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html') 


def user_logout(request):
    logout(request)
    return redirect('home')