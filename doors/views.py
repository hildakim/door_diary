from django.shortcuts import render, redirect, get_object_or_404
from .models import PhotoDiary
from django.utils import timezone
from .forms import PhotoDiaryForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    keyword = request.GET['keyword']
    search_list = PhotoDiary.objects.filter(Q(body__icontains=keyword)).distinct()
    paginator = Paginator(search_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'search.html', {'search_list':search_list, 'posts': posts})

def room(request):
    allPost = PhotoDiary.objects.all()
    diary_list = PhotoDiary.objects.all()
    paginator = Paginator(diary_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'room.html', {'allPost': allPost, 'posts':posts})

def detail(request, id):
    blogPost = get_object_or_404(PhotoDiary, pk = id)
    return render(request, 'detail.html', {'blogPost':blogPost})
    
def new(request):
  if request.method == 'POST':
    form = PhotoDiaryForm(request.POST, request.FILES)
    if form.is_valid():
      new_blog = form.save(commit=False)
      new_blog.upload_date = timezone.now()
      new_blog.save()
      return redirect('doors:detail', new_blog.id)
    return redirect('home')
  else:
    form = PhotoDiaryForm()
    return render(request, 'new.html', {'form': form})
    

def edit(request, id):
  post = get_object_or_404(PhotoDiary, pk = id)
  if request.method == 'GET': 
    blog_form = PhotoDiaryForm(instance = post)
    return render(request, 'edit.html', {'edit_form':blog_form})
  else: 
    blog_form = PhotoDiaryForm(request.POST, request.FILES, instance = post)
    if blog_form.is_valid():
      edit_blog = blog_form.save(commit=False)
      edit_blog.upload_date = timezone.now()
      edit_blog.save()
    return redirect('/doors/post/'+str(id))


def delete(request, id):
  delete_review = PhotoDiary.objects.get(id = id)
  delete_review.delete()
  return redirect('home')