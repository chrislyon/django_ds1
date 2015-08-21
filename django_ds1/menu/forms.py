# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, MultiField, HTML


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'post'
    helper.form_action = '/accounts/login/'
    helper.layout = Layout(
        Field('username', css_class='input-xlarge'),
        Field('password', rows="3", css_class='input-xlarge'),
		Hidden('next', '/ds'),
        FormActions(
            Submit('save_changes', 'Connexion', css_class="btn-primary"),
            Submit('cancel', 'Annulation'),
        )
    )
