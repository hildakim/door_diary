from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')