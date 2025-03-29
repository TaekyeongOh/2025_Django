from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from user.forms import SignUpForm

@login_required
def home(request):
    return render(request, "templates/home.html", {})

def signup_view(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/user/accounts/login/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})