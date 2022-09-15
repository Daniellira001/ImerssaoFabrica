from django.shortcuts import render
from django.http import HttpResponse

def chiclete(request):
    return render(request, template_name='blog/home.html')

def jujuba(request):
    html = "<html><body><h1>jujuba</h1></body></html>"
    return HttpResponse(html)

# Create your views here.
