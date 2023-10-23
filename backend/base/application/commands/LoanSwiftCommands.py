from django import forms
from ...domain.valueObjects.Genders import Genders
from django.core.validators import RegexValidator

alphabetical = RegexValidator(r'^[a-zA-Z]*$', "Only alphanumeric characters are allowed.")

class CreateLoanSwiftCommand(forms.Form):
    document_number =  forms.IntegerField( min_value=1 )
    first_name = forms.CharField( min_length=3, max_length=50, validators=[alphabetical] ) 
    last_name = forms.CharField( min_length=3, max_length=50, validators=[alphabetical] )
    gender = forms.ChoiceField( choices=Genders.choices )
    email = forms.EmailField()
    amount = forms.IntegerField( min_value=1 )


class DeleteLoanSwiftCommand(forms.Form):
    id = forms.UUIDField()

class PatchLoanSwiftCommand(forms.Form):
    id = forms.UUIDField( required=True )
    first_name = forms.CharField( min_length=3, max_length=50, validators=[alphabetical], required=False ) 
    last_name = forms.CharField( min_length=3, max_length=50, validators=[alphabetical], required=False )
    gender = forms.ChoiceField( choices=Genders.choices, required=False )
    email = forms.EmailField( required=False )
    amount = forms.IntegerField( min_value=1, required=False )