from django.shortcuts import render

# Create your views here.
# 메인 페이지를 응답하는 함수
def index(request):
    return render(request, 'articles/index.html')