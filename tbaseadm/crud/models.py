from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

## -------------------------------------------------
## Meta Class contenant certaines donnees de bases
## -------------------------------------------------
class HoroDatage(models.Model):
	h_datcre = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
	h_datmod = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

	statut = models.BooleanField(verbose_name='Actif', default=True)

	class Meta:
		abstract = True

## ---------------------
## infra / Serveurs 
## ---------------------
class Serveur(HoroDatage):
	OS_TYPES = (
		('UNIX', 'UNIX'),
		('WIN', 'WINDOWS'),
		('AUT', 'AUTRES')
	)
	MACH_TYPES = (
		( 'VM', 'Machine Virtuelle'),
		('PHY', 'Physique')
	)
	S_Nom = models.CharField(max_length=30, verbose_name='Nom')
	S_Type = models.CharField(max_length=3, choices=MACH_TYPES, default='PHY', verbose_name='Type')
	S_IP = models.GenericIPAddressField(default='127.0.0.1', verbose_name='Adr IP')
	S_OSTYPE = models.CharField(max_length=5, choices=OS_TYPES, default='UNIX', verbose_name='Famille OS')
	S_OSVersion = models.CharField(max_length=30, blank=True, verbose_name='OS Version')
	S_Desc = models.TextField(default=' ',blank=True, verbose_name='Description')

	def __unicode__(self):
		return "%s:%s" % (self.S_Nom, self.S_Type)
