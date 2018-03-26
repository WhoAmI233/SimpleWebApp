from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def get_text_from_target(request):
    return render(
        request,
        'index.html',
        {'get_text_from_target': request.GET.get('get_text_from_target', "")}
    )


