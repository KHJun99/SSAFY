from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title","description","rating","author")
        labels = {
            "title":"제목","description":"설명","rating":"회원 리뷰 평점(0~5)","author":"저자",
        }
