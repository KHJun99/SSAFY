
# crawlings/urls.py
from django.urls import path
from . import views

app_name = 'crawlings'
urlpatterns = [
    path('index/', views.index, name='index'),          # F01
    path('fetch/', views.fetch, name='fetch'),          # F02 트리거
    path('list/', views.comment_list, name='list'),     # F03
    path('delete/<int:pk>/', views.delete_comment, name='delete'),  # F04
]
