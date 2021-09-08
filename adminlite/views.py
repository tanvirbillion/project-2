from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth import login as auth_login, authenticate, logout
#from django.contrib.auth.decorators import login_required
#from verify_email.email_handler import send_verification_email

#from .forms import LoginForm, SignUpForm


# Create your views here.
def index(request):
    print(request.user.username)
    return render(request, 'dashboard/index.html')

def main(request):
    return render(request, 'dashboard/main.html')