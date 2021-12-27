from django.urls import path

from texts.views import text, book

urlpatterns = [
    path('text/<slug:slug>/', text),
    path('book/<slug:slug>/', book),
]