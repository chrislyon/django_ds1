# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup
from ckeditor.widgets import CKEditorWidget

from .models import DService


class DS_Form(forms.ModelForm):

	DS_Type 			= forms.ChoiceField( label='Type de la Demande', choices=DService.TYPE_DS, initial = 'ASS')
	DS_TiersDemandeur	= forms.CharField( label='Demandeur')
	DS_TiersFacture		= forms.CharField( label='Facture a')
	DS_Sujet			= forms.CharField( label='Objet' )
	#DS_Desc				= forms.CharField( label='Description', widget = forms.Textarea(), )
	DS_Desc				= forms.CharField( label='Description', widget=CKEditorWidget() )
	DS_Statut			= forms.ChoiceField( label='Statut', choices=DService.STATUT_DS, initial = 'NEW')
	DS_Assigne			= forms.CharField( label='Asssigne a' )
	DS_Priorite			= forms.CharField( label='Priorité' )
	DS_Horo_Debut		= forms.CharField( label='Debut' )
	DS_Horo_Fin			= forms.CharField( label='Fin' )
	DS_TempsEstime		= forms.CharField( label='Temps Estime' )
	DS_TempsRealise		= forms.CharField( label='Temps Realise' )
	DS_PC_Realise		= forms.CharField( label='Realise' )
	DS_Echeance			= forms.CharField( label='Echeance' )

	# Uni-form
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.form_method = 'post'


	lay_2 = Layout(
		Fieldset( 'Demandeur',
			Div(
				Div('DS_Type', css_class='span5'), Div('DS_TiersDemandeur', css_class='span5'), Div('DS_TiersFacture', css_class='span5')
				),
			),
		Fieldset( 'Description',
			Div('DS_Sujet', css_class='form-control'),
			Div('DS_Desc'),
			),
		Fieldset( 'Temps et Statut',
				Div(
					Div('DS_Statut', css_class='span5'),
					Div('DS_Assigne', css_class='span5'),
					Div('DS_Priorite', css_class='span5'),
					),
				Div(
					Div('DS_Horo_Debut', css_class='span5'),
					Div('DS_Horo_Fin', css_class='span5'),
					),
				Div(
					Div('DS_TempsEstime', css_class='span5'),
					Div('DS_Echeance', css_class='span5'),
					Div('DS_TempsRealise', css_class='span5'),
					Div('DS_PC_Realise', css_class='span5'),
					),
			),
		FormActions(
			Button('cancel', 'Annulation'),
			Submit('save_changes', 'Valider', css_class="btn-primary"),
		)
	)

	helper.layout = lay_2

	class Meta:
		model = DService
		fields = '__all__'

## Essai de Layout
#
#	lay_3 = Layout(
#			Field('DS_Type'),
#			Field('DS_TiersDemandeur'),
#			Field('DS_TiersFacture'),
#			Field('DS_Sujet'),
#			Field('DS_Desc'),
#			Field('DS_Statut'),
#			Field('DS_Assigne'),
#			Field('DS_Priorite'),
#			Field('DS_Horo_Debut'),
#			Field('DS_Horo_Fin'),
#			Field('DS_TempsEstime'),
#			Field('DS_TempsRealise'),
#			Field('DS_PC_Realise'),
#			Field('DS_Echeance'),
#		FormActions(
#			Submit('save_changes', 'Valider', css_class="btn-primary"),
#			Submit('cancel', 'Annulation'),
#		)
#	)


#	lay_1 = Layout(
#		Fieldset( 'Demandeur',
#			Field('DS_Type', label='Type de Demande' ),
#			Field('DS_TiersDemandeur', css_class='input-xlarge'),
#			Field('DS_TiersFacture', css_class='input-xlarge'),
#			),
#		Fieldset( 'Description',
#			Field('DS_Sujet', css_class='input-xlarge'),
#			Field('DS_Desc', css_class='input-xlarge'),
#		),
#		Fieldset( 'Statut',
#			Field('DS_Statut', css_class='input-xlarge'),
#			Field('DS_Assigne', css_class='input-xlarge'),
#			Field('DS_Priorite', css_class='input-xlarge'),
#		),
#		Fieldset( 'Temps',
#			Field('DS_Horo_Debut', css_class='input-xlarge'),
#			Field('DS_Horo_Fin', css_class='input-xlarge'),
#			Field('DS_TempsEstime', css_class='input-xlarge'),
#			Field('DS_TempsRealise', css_class='input-xlarge'),
#			Field('DS_PC_Realise', css_class='input-xlarge'),
#			Field('DS_Echeance', css_class='input-xlarge'),
#		),
#		FormActions(
#			Submit('save_changes', 'Valider', css_class="btn-primary"),
#			Submit('cancel', 'Annulation'),
#		)
#	)

