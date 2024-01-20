from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import Movie


# Create your views here.
def index(request):
    obj = Movie.objects.all()
    return render(request, "index.html", {'result': obj})


def detail(request,id):
    details = Movie.objects.get(id=id)
    return render(request, "detail.html",{'details':details})

def update(request,id):
    eachtask = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=eachtask)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'eachtask': eachtask})

def delete(request,id):
    if request.method == 'POST':
        dtask = Movie.objects.get(id=id)
        dtask.delete()
        return redirect('/')
    return render(request, 'delete.html')

def add(request):

    if request.method == "POST":
        movie_name = request.POST.get('movie_name', '')
        movie_desc = request.POST.get('movie_desc', '')
        movie_year = request.POST.get('movie_year', '')
        movie_image = request.FILES['movie_image']

        movie_item = Movie(movie_name=movie_name, movie_desc=movie_desc, movie_year=movie_year,movie_image=movie_image)
        movie_item.save()
        return redirect('/')
    return render(request, 'add.html')


