from ...domain.entities.LoanSwift import LoanSwift

class LoanSwiftRepository():
    model = LoanSwift

    @classmethod
    def list(self):
        return self.model.objects.all()
    
    @classmethod
    def save( self, command ):
        return self.model(**command.data).save()
    
    @classmethod
    def delete(self, id: str):
        LoanSwiftSaved = self.model.objects.filter(id=id)

        if (LoanSwiftSaved.count != 1):
            raise Exception("No se ah encontrado el Loan")
        
        return LoanSwiftSaved.delete()

