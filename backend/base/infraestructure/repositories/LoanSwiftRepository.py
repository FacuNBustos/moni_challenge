from ...domain.entities.LoanSwift import LoanSwift
from datetime import datetime

class LoanSwiftRepository():
    model = LoanSwift

    @classmethod
    def list( self ):
        return self.model.objects.filter( deleted_at=None )
    
    @classmethod
    def save( self, loanSwift ):
        self.model( **loanSwift ).save()

    @classmethod
    def findById( self, id:str ):
        return self.model.objects.filter( id=id, deleted_at = None )
    
    @classmethod
    def delete(self, id:str ):
        loanSwiftSaved = self.model.objects.get( id=id )
        loanSwiftSaved.deleted_at = datetime.now()
        loanSwiftSaved.save()
        
    @classmethod
    def patch( self, changes ):
        loanSwiftSaved = self.model.objects.get( id=changes["id"] )
        loanSwiftSaved.first_name = changes["first_name"] if "first_name" in changes else loanSwiftSaved.first_name
        loanSwiftSaved.last_name = changes["last_name"] if "last_name" in changes else loanSwiftSaved.last_name
        loanSwiftSaved.gender = changes["gender"] if "gender" in changes else loanSwiftSaved.gender
        loanSwiftSaved.email = changes["email"] if "email" in changes else loanSwiftSaved.email
        loanSwiftSaved.amount = changes["amount"] if "amount" in changes else loanSwiftSaved.amount
        loanSwiftSaved.save()

