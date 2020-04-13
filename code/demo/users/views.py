from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    str = '{"name" : "jesse"}'

    return HttpResponse(str,
                        content_type="application/json",
                        status=400)


def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.getlist('a')


    print(a)
    print(b)
    print(c)

    return HttpResponse('qs')
