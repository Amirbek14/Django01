from django.http import HttpResponse
from django.shortcuts import render




def main(a):
    return HttpResponse("Hello world")

def main2(request):
    return render(request, 'index.py')