from django.contrib import admin

from ds.models import DService

# Register your models here.
class DServiceAdmin(admin.ModelAdmin):
	list_display = ('DS_Type', 'DS_TiersDemandeur', 'DS_Sujet', 'statut')
	list_filter = ('DS_Type', 'DS_TiersDemandeur', 'DS_Sujet', 'statut')
	search_fields = ['DS_Type', 'DS_TiersDemandeur', 'DS_Sujet' ]

admin.site.register(DService, DServiceAdmin)

