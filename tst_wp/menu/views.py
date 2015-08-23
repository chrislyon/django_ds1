from django.shortcuts import render

# Create your views here.

def home(request):
	title = 'DS / MENU PRINCIPAL'
	return render(request, 'menu/home.html', {'page_title':title})

def about(request):
	title = 'DS / ABOUT'
	return render(request, 'menu/about.html', {'page_title':title})

