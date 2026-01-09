from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from Myapplication.forms import RegisterForm, SignUpForm, LoginForm
from Myapplication.models import Data

# ---------------------------
# Authentication Views
# ---------------------------

def signup_view(request):
    """Signup page for new users"""
    if request.user.is_authenticated:
        return redirect('Home')
    
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Signup failed! Please correct the errors.")
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    """Login page for users"""
    if request.user.is_authenticated:
        return redirect('Home')
    
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """Logout user"""
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


# ---------------------------
# CRUD Views (Require Login)
# ---------------------------

@login_required(login_url='login')
def home(request):
    """Dashboard: display form + table"""
    form = RegisterForm()
    datas = Data.objects.all()
    return render(request, 'index.html', {'form': form, 'datas': datas})


@login_required(login_url='login')
def addData(request):
    """Add a new Data record"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
        else:
            messages.error(request, "Failed to add record! Check the input.")
    return redirect('Home')


@login_required(login_url='login')
def updateData(request, id):
    """Update an existing Data record"""
    data = get_object_or_404(Data, id=id)
    form = RegisterForm(instance=data)
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('Home')
        else:
            messages.error(request, "Failed to update record! Check the input.")
    
    return render(request, 'update.html', {'form': form})


@login_required(login_url='login')
def deleteData(request, id):
    """Delete a Data record"""
    data = get_object_or_404(Data, id=id)
    if request.method == 'POST':
        data.delete()
        messages.success(request, "Record deleted successfully!")
    return redirect('Home')
