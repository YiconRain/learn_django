from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# 登录视图
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_view')
            else:
                messages.error(request, "用户名或密码无效")
    else:
        form = AuthenticationForm()

    return render(request, 'web_app/login.html', {'form': form})

# 注册视图
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "注册成功，请登录")
            return redirect('login_view')
    else:
        form = UserCreationForm()

    return render(request, 'web_app/register.html', {'form': form})

# 注销视图
def logout_view(request):
    logout(request)
    return redirect('login_view')
