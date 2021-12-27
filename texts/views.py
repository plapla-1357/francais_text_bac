from django.shortcuts import render, HttpResponse

# Create your views here.
from texts.models import Book, Text, Sequence, Text_interpretation


def main_page(request):
    user = request.user
    texts = Text.objects.all()
    sequences = Sequence.objects.all()
    books = Book.objects.all()
    return render(request, "texts/main.html",
                  context={"texts": texts,
                           "sequences": sequences,
                           "books": books,
                           "user": user})


def book(request, slug):
    livre = Book.objects.get(slug_title=slug)
    return render(request, "texts/book_page.html", context={"book": livre})


def text(request, slug):
    text = Text.objects.get(slug_name=slug)
    Interpretations = Text_interpretation.objects.all()
    interpretations = [i for i in Interpretations if i.Text == text]
    return render(request, 'texts/text_page.html',
                  context={"Text": text,
                           "Interpretations": interpretations,
                           'user': request.user})
