from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request):
    res = '<h1>Main page</h1>'
    return HttpResponse(res)


def about(request):
    res = '<h1>About me</h1>'
    return HttpResponse(res)

