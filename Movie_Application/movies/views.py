from django.shortcuts import render, redirect
from .models import Movie
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def movie_list(request):
	movies = Movie.objects.all().order_by('date')
	return render(request,'movies/movie_list.html',{'movies':movies})

def movie_detail(request,slug):
	movie = Movie.objects.get(slug=slug)
	return render(request,'movies/movie_detail.html',{'movie':movie})

@login_required(login_url="/accounts/login/")
def movie_create(request):
	if request.method == 'POST':
		form = forms.CreateMovie(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			# instance.author = request.user
			instance.save()
			print(instance)
			return redirect('movies:list')
	else:
		form = forms.CreateMovie()
	return render(request,'movies/movie_create.html',{'form':form})
