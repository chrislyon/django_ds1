from django.shortcuts import render

# Create your views here.

def home(request):
	title = 'P1 / MENU PRINCIPAL'
	return render(request, 'p1/home.html', {'page_title':title})

def about(request):
	title = 'P1 / ABOUT'
	return render(request, 'p1/about.html', {'page_title':title})

def f1(request):
	title = 'P1 / FORM1'
	return render(request, 'p1/form1.html', {'page_title':title})

def t1(request):
	title = 'T1 / TABLE 1'
	return render(request, 'p1/table.html', {'page_title':title})

