from django.shortcuts import render

# Create your views here.

def bash(request):
    return render(request,'bash.html')