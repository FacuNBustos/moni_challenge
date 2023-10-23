from django.db import models
from uuid import uuid4
from ..valueObjects.Genders import Genders

class LoanSwift( models.Model ):
    id = models.UUIDField( unique=True, primary_key=True, default=uuid4, editable=False )
    document_number = models.IntegerField( editable=False )
    first_name = models.CharField( max_length=50 )
    last_name = models.CharField( max_length=50 )
    gender = models.CharField( max_length=20, choices=Genders.choices )
    email = models.EmailField( max_length=250 )
    amount = models.IntegerField()

    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )
    deleted_at = models.DateTimeField( null=True, blank=True )
