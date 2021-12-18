from django.urls import path

urlpatterns = [
    path('text/<slug:text_name>', text)
]