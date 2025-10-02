# books/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, 'books/index.html', context)

@login_required  # 명세: 생성/수정/삭제 = 로그인 필요
def create(request):
    form = BookForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        book = form.save()
        return redirect("books:detail", book.pk)
    return render(request, "books/create.html", {"form": form})

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/detail.html', {"book": book})

@login_required
def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("books:detail", book.pk)
    return render(request, "books/update.html", {"form": form, "book": book})

@login_required
@require_POST  # 삭제는 POST only (안전)
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("books:index")
