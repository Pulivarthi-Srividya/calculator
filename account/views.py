from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Register view
def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')
        if password != confpassword:
            return render(request, 'register.html', {'result': 'ERROR'}) 
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

# Login view
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# Home view (choose one behavior)
def home(request):
    return render(request, 'home.html')  # or redirect('calculator')

# Calculator logic
def calculator(request):
    result = None
    if request.method == 'POST':
        a = int(request.POST.get('num1'))
        b = int(request.POST.get('num2'))
        o = request.POST.get('op')
        if o == 'add':
            result = a + b
        elif o == 'subtract':
            result = a - b
        elif o == 'multiply':
            result = a * b
        return redirect('result', result=result)  # passes result via URL
    return render(request, 'calculator.html')

# Result display
def result(request, result):
    return render(request, 'result.html', {'result': result})

# Logout
def logoutpage(request):
    logout(request)
    return redirect('login')
