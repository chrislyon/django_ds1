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
	DS_Desc				= forms.CharField( label='Description', widget=CKEditorWidget() )
	DS_Statut			= forms.ChoiceField( label='Statut', choices=DService.STATUT_DS, initial = 'NEW')
	DS_Assigne			= forms.CharField( label='Asssigne a' )
	DS_Priorite			= forms.CharField( label='Priorité' )
	#DS_Horo_Debut		= forms.DateTimeField( label='Debut', widget=forms.TextInput( attrs={ 'class': 'datepicker' } ))
	#DS_Horo_Fin			= forms.DateTimeField( label='Fin' )
	DS_TempsEstime		= forms.CharField( label='Temps Estime' )
	DS_TempsRealise		= forms.CharField( label='Temps Realise' )
	DS_PC_Realise		= forms.CharField( label='Realise' )
	#DS_Echeance			= forms.CharField( label='Echeance' )

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
		Fieldset( 'Debut et Fin',
			HTML( "<table>"),
			HTML( "<tr><td>"),
				Field('DS_Horo_Debut', css_class='dp1'),
				Field('DS_Horo_Fin', css_class='dp1'),
			HTML( "</td><td>"),
				Field('DS_Echeance', css_class='dp1'),
			HTML( "</td></tr>"),
			HTML( "</table>"),
			),
		Fieldset( 'Temps et Statut',
				Div(
					Div('DS_Statut', css_class='span5'),
					Div('DS_Assigne', css_class='span5'),
					Div('DS_Priorite', css_class='span5'),
					),
				Div(
					Div('DS_TempsEstime', css_class='span5'),
					Div('DS_TempsRealise', css_class='span5'),
					Div('DS_PC_Realise', css_class='span5'),
					),
			),
		FormActions(
			Button('cancel', 'Annulation', onclick="javascript:history.back();"),
			Submit('save_changes', 'Valider', css_class="btn-primary"),
		)
	)

	helper.layout = lay_2

	## Necessaire pour une ModelForm
	class Meta:
		model = DService
		fields = '__all__'
