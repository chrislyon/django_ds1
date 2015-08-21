from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
from .forms import LoginForm

def home(request):
	title = 'DS / MENU PRINCIPAL'
	return render(request, 'menu/home.html', {'page_title':title, 'form':LoginForm()})

def about(request):
	title = 'DS / ABOUT'
	return render(request, 'menu/about.html', {'page_title':title})

def logout_view(request):
	logout(request)
	return redirect('/')
