from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("update/", views.update_view, name="update"),
    path("delete/", views.delete_view, name="delete"),
    path("change-password/", views.change_password_view, name="change_password"),
]
