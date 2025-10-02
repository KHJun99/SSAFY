from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User

class LoginForm(AuthenticationForm):
    pass  # 기본 유효성 검증 사용

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")  # 필요 시 email optional

class ProfileUpdateForm(UserChangeForm):
    password = None  # 화면에 비밀번호 해시 안 노출
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
