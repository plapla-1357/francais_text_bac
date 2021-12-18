from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, "texts/text.html")


def text(request, text_name):
    # text_data = text.objects.get(name=text_name)
    return render(request, "texts/text.html", context={"titre": text_name})