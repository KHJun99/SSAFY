from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

@require_http_methods(["GET"])  # F12
def index(request):
    books = Book.objects.order_by("-id")
    return render(request, "books/index.html", {"books": books})

@login_required
@require_http_methods(["GET","POST"])  # F13
def create(request):
    form = BookForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        book = form.save()
        return redirect("books:detail", book.pk)
    return render(request, "books/create.html", {"form": form})

@require_http_methods(["GET"])  # F14
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/detail.html", {"book": book})

@login_required
@require_http_methods(["GET","POST"])  # F15
def update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("books:detail", book.pk)
    return render(request, "books/update.html", {"form": form, "book": book})

@login_required
@require_POST  # F16 + NF02
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("books:index")
