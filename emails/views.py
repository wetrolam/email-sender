from django.shortcuts import render

def new(request):
    return render(request, 'emails/new.html')

def send(request):
    return render(request, 'emails/send.html')
