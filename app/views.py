from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mom(request):
    return HttpResponse('<h1><marquee> my mom loves their children </h1></marquee>')
