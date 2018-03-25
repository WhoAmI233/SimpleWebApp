from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def hello_page(request):
    return render(
        request,
        'index.html',
        {'hello_words': request.GET.get('hello_words', "")}
    )


