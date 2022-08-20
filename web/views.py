from django.shortcuts import render
from .models import Roman
# Create your views here.

def home(request):
	cotext = {
		"AllRoman":Roman.objects.all().order_by('-vote')
	} 
	return render(request, 'web/home.html', cotext)

def post(request,slug):
	p = Roman.objects.get(slug=slug)
	p.vote += 1
	p.save()
	cotext = {
		"Roman":Roman.objects.get(slug=slug),
		"User":str(p.user),
	} 
	return render(request, 'web/post.html', cotext)
