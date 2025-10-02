from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .forms import LoginForm, SignupForm, ProfileUpdateForm

@require_http_methods(["GET","POST"])  # F06
def login_view(request):
    if request.user.is_authenticated:
        return redirect("books:index")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("books:index")
    return render(request, "accounts/login.html", {"form": form})

@require_POST  # F07 + NF02
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("books:index")

@require_http_methods(["GET","POST"])  # F08
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("books:index")
    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)  # 가입 후 로그인
        return redirect("books:index")
    return render(request, "accounts/signup.html", {"form": form})

@login_required
@require_http_methods(["GET","POST"])  # F09
def update_view(request):
    form = ProfileUpdateForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("books:index")
    return render(request, "accounts/update.html", {"form": form})

@login_required
@require_POST  # F10 + NF02
def delete_view(request):
    request.user.delete()
    logout(request)
    return redirect("books:index")

@login_required
@require_http_methods(["GET","POST"])  # F11
def change_password_view(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        # 비밀번호 변경 후 로그인 유지
        update_session_auth_hash(request, user)
        return redirect("books:index")
    return render(request, "accounts/change_password.html", {"form": form})
