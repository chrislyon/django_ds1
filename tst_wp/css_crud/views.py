# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from css_crud.models import Serveur

class ServeurForm(ModelForm):
    class Meta:
        model = Serveur
        fields = [ 'S_Nom', 'S_Type', 'S_IP', 'S_OSTYPE', 'S_OSVersion', 'S_Desc' ]

def populate(nb):
	for x in range(1,nb):
		s = Serveur(S_Nom="TST%03d" % x, S_OSVersion='RH6')
		print(s.S_Nom)
		s.save()

def crud_list(request, template_name='css_crud/crud_list.html'):
    cruds = Serveur.objects.all()
    data = {}
    data['object_list'] = cruds
    return render(request, template_name, data)

def crud_create(request, template_name='css_crud/crud_form.html'):
    form = ServeurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('css_crud_list')
    return render(request, template_name, {'form':form})

def crud_update(request, pk, template_name='css_crud/crud_form.html'):
    crud = get_object_or_404(Serveur, pk=pk)
    form = ServeurForm(request.POST or None, instance=crud)
    if form.is_valid():
        form.save()
        return redirect('css_crud_list')
    return render(request, template_name, {'form':form})

def crud_delete(request, pk, template_name='css_crud/crud_confirm_delete.html'):
    crud = get_object_or_404(Serveur, pk=pk)    
    if request.method=='POST':
        crud.delete()
        return redirect('css_crud_list')
    return render(request, template_name, {'object':crud})
