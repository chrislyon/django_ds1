from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ds.models import DService

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
			] )
	my_data['data'] = data
	nb = len(data)
	my_data['recordsTotal'] = nb
	my_data['recordsFiltered'] = nb

	# Et on les envoie
	return JsonResponse(my_data)
