from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.forms import ModelForm
from ds.models import DService
from ds.forms import DS_Form

## Liste / Datatables
@login_required(login_url='/accounts/login/')
def home(request):
	title = 'DS / MAIN PAGE'
	return render(request, 'ds/home.html', {'page_title':title })

## Pop liste / Datatables avec du json 
@login_required(login_url='/accounts/login/')
def data(request):
	# Ici on prend toute la table
	# On construit les donnes json
	my_data = {}
	my_data['draw'] = 1
	data = []
	## Mapping ORM Django avec requete ajax
	for R in DService.objects.all():
		modif  = '<a href="/ds/ds_upd/%s">' % R.id
		modif += '<img border="0" alt="Modif" src="/static/icons/icon_modif.png" width="15" height="15">'
		modif += '</a>'
		delrec  = '<a href="/ds/ds_del/%s">' % R.id
		delrec += '<img border="0" alt="delete" src="/static/icons/icon_delete.png" width="15" height="15">'
		delrec += '</a>'
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
			modif,
			delrec
			] )
	my_data['data'] = data
	nb = len(data)
	my_data['recordsTotal'] = nb
	my_data['recordsFiltered'] = nb

	# Et on les envoie
	return JsonResponse(my_data)

## Nouvelle demande 
@login_required(login_url='/accounts/login/')
def ds_create(request, template_name='ds/ds_form.html'):
    form = DS_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ds_home')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def ds_update(request, pk, template_name='ds/ds_form.html'):
    crud = get_object_or_404(DService, pk=pk)
    form = DS_Form(request.POST or None, instance=crud)
    if form.is_valid():
        form.save()
        return redirect('ds_home')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def ds_delete(request, pk, template_name='ds/confirm_delete.html'):
    crud = get_object_or_404(DService, pk=pk)    
    if request.method=='POST':
        crud.delete()
        return redirect('ds_home')
    return render(request, template_name, {'object':crud})
