from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.forms import ModelForm
from ds.models import DService
from ds.forms import DS_Form

#class DS_Form(ModelForm):
#	class Meta:
#		model = DService
#		fields = [ 	'DS_Type', 
#					'DS_TiersDemandeur', 
#					'DS_TiersFacture', 
#					'DS_Sujet', 
#					'DS_Desc', 
#					'DS_Statut',
#					'DS_Assigne',
#					'DS_Priorite',
#					'DS_Horo_Debut',
#					'DS_Horo_Fin',
#					'DS_TempsEstime', 
#					'DS_TempsRealise', 
#					'DS_PC_Realise', 
#					'DS_Echeance'
#				]
#

@login_required(login_url='/accounts/login/')
def home(request):
	title = 'DS / MAIN PAGE'
	return render(request, 'ds/home.html', {'page_title':title })

@login_required(login_url='/accounts/login/')
def data(request):
	# Ici on prend toute la table
	# On construit les donnes json
	my_data = {}
	my_data['draw'] = 1
	data = []
	## Mapping ORM Django avec requete ajax
	for R in DService.objects.all():
		modif  = '<a href="/ds/modif/%s">' % R.id
		modif += '<img border="0" alt="Modif" src="/static/icons/icon_modif.png" width="15" height="15">'
		modif += '</a>'
		data.append( [ 
			R.DS_Type, 
			R.DS_TiersDemandeur, 
			R.DS_TiersFacture, 
			R.DS_Sujet, 
			R.DS_Statut, 
			R.DS_Assigne, 
			R.DS_Priorite, 
			R.DS_TempsEstime, 
			R.DS_TempsRealise,
			R.DS_Echeance,
			modif
			] )
	my_data['data'] = data
	nb = len(data)
	my_data['recordsTotal'] = nb
	my_data['recordsFiltered'] = nb

	# Et on les envoie
	return JsonResponse(my_data)

#@login_required(login_url='/accounts/login/')
#def ds_create(request):
#	title = 'Creation Demande de Service'
#	return render(request, 'ds/ds_form.html', {'page_title':title })

@login_required(login_url='/accounts/login/')
def ds_create(request, template_name='ds/ds_form.html'):
    form = DS_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ds_home')
    return render(request, template_name, {'form':form})

### A Modifier

@login_required(login_url='/accounts/login/')
def ds_update(request, pk, template_name='crud/crud_form.html'):
    crud = get_object_or_404(Serveur, pk=pk)
    form = ServeurForm(request.POST or None, instance=crud)
    if form.is_valid():
        form.save()
        return redirect('crud_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def ds_delete(request, pk, template_name='crud/crud_confirm_delete.html'):
    crud = get_object_or_404(Serveur, pk=pk)    
    if request.method=='POST':
        crud.delete()
        return redirect('crud_list')
    return render(request, template_name, {'object':crud})
