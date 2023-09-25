from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movies
from .forms import MovieForm
# Create your views here.

def home(request):
    movies= Movies.objects.all()
    context= {
        'movies':movies
    }
    return render(request,'home.html',context)

def movie_details(request,id_movie):
    dt=Movies.objects.get(id=id_movie)
    return render(request,'details.html',{'movie_detail':dt})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        year=request.POST.get('year')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        added_movie=Movies(name=name,year=year,description=description,image=image)
        added_movie.save()
    return render(request,'add.html')

def update(request, id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'update.html', {'form': form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        dl=Movies.objects.get(id=id)
        dl.delete()
        return redirect('/')
    return render(request,'delete.html')
