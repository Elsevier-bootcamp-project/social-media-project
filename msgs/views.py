from django.shortcuts import render

from django.http import HttpResponse

def messages(request):
    return render (request,'messages/messages.html')
