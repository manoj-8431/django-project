from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

User = get_user_model()

#register
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords dont' match!")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register')
        
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email
        )
        messages.success(request, "Account created! You can now login.")
        return redirect('login')
    return render(request, "myapp/register.html")

#login
def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username_or_email, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    return render(request, "myapp/login.html")

#home
def home_view(request):
    return render(request, "myapp/home.html")

#order
@login_required(login_url='home')
def order_view(request):
    if request.user.is_authenticated:
        return render(request, "myapp/order.html")
    else:
        messages.error(request, "You need to Login to make an order!")
        return redirect('login')

#account
@login_required(login_url='home')
def account_view(request):
    if request.user.is_authenticated:
        return render(request, "myapp/account.html")
    else:
        return redirect('login')