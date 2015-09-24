from django.contrib import admin

# Register your models here.
from crud.models import Serveur

# Register your models here.
class ServeurAdmin(admin.ModelAdmin):
	list_display = ('S_Nom', 'S_Type', 'S_IP', 'S_OSTYPE', 'S_OSVersion', 'statut')
	list_filter = ('S_Nom', 'S_Type', 'S_IP', 'statut')
	search_fields = ['S_Nom', 'S_IP' ]

admin.site.register(Serveur, ServeurAdmin)


