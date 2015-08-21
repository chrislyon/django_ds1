from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
	title = 'DS / MAIN PAGE'
	return render(request, 'ds/home.html', {'page_title':title })
