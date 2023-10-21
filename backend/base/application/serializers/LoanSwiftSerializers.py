from rest_framework import serializers
from ...domain.entities.LoanSwift import LoanSwift

class LoanSwiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanSwift 
        exclude = [ 'created_at', 'updated_at', 'deleted_at' ]
        