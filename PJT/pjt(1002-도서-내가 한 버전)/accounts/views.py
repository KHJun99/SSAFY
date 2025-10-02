# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserChangeForm


def login(request):
    # 이미 로그인 상태면 메인으로
    if request.user.is_authenticated:
        return redirect('books:index')

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 로그인 후 next 우선 이동
            next_url = request.POST.get('next') or request.GET.get('next')
            messages.success(request, "로그인되었습니다.")
            return redirect(next_url or 'books:index')
        else:
            messages.error(request, "아이디/비밀번호를 확인해 주세요.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        # 템플릿에서 hidden input 으로 전달 가능
        'next': request.GET.get('next', ''),
    })


# (권장) 로그아웃은 POST-only로 운영. 기존 GET을 유지하려면 데코레이터 제거.
@require_POST
def logout(request):
    auth_logout(request)
    messages.info(request, "로그아웃되었습니다.")
    return redirect('books:index')


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "회원가입이 완료되었습니다. 로그인해 주세요.")
            # 자동 로그인 원하면 아래 두 줄 사용:
            # auth_login(request, user)
            # return redirect('books:index')
            return redirect('accounts:login')
        else:
            messages.error(request, "입력값을 확인해 주세요.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


@login_required
@require_POST
def delete(request):
    """
    [회원 탈퇴] POST-only
    - GET으로 탈퇴가 되지 않도록 보호
    """
    request.user.delete()
    messages.warning(request, "회원 탈퇴가 완료되었습니다.")
    return redirect('books:index')


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "회원정보가 수정되었습니다.")
            return redirect("accounts:update")
        else:
            messages.error(request, "입력값을 확인해 주세요.")
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, "accounts/update.html", {'form': form})


@login_required
def change_password(request):
    """
    [비밀번호 변경]
    - 로그인 필수
    - 변경 후 세션 유지(update_session_auth_hash)
    """
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션 유지
            messages.success(request, "비밀번호가 변경되었습니다.")
            return redirect("accounts:update")
        else:
            messages.error(request, "입력값을 확인해 주세요.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "accounts/change_password.html", {"form": form})
