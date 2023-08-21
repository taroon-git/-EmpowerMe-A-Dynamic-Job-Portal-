from django.shortcuts import render

# Create your views here.

def IndexView(request):
    return render(request,'index.html')

def Signup(request):
    return render(request,'signup.html')