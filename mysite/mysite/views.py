

from django.http import HttpResponse


def divert_text(request):
    return HttpResponse("Hello to Maya's world")