# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "description", "rating", "author")
        labels = {
            "title": "제목",
            "description": "설명",
            "rating": "회원 리뷰 평점(0~5)",
            "author": "저자",
        }
        help_texts = {
            "rating": "0에서 5 사이의 정수만 입력하세요.",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "도서 제목"}),
            "author": forms.TextInput(attrs={"class": "form-control", "placeholder": "저자"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "도서 설명"}),
            "rating": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 5}),
        }
