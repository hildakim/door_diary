from django.shortcuts import render, redirect, get_object_or_404
from .models import PhotoDiary
from django.utils import timezone
from .forms import PhotoDiaryForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'home.html')