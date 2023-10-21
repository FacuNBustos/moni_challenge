from ..commands.LoanSwiftCommands import CreateLoanSwiftCommand
from ...infraestructure.repositories.LoanSwiftRepository import LoanSwiftRepository
from ..serializers.LoanSwiftSerializers import LoanSwiftSerializer
from ...infraestructure.services.LoanSwiftService import AcceptanceConsultation

def ListLoanSwiftHandler():
    loandSwiftsSaved = LoanSwiftRepository.list()
    
    payload = []
    for loanSwift in loandSwiftsSaved:
        payload.append(LoanSwiftSerializer(loanSwift).data)

    return payload

def CreateLoanSwiftHandler( command:CreateLoanSwiftCommand ):
    loanIsAccept = AcceptanceConsultation(command.data['document_number'])
    if (loanIsAccept == False):
        raise Exception("handler", "No fue aceptado")
    
    return LoanSwiftRepository.save(command)

    
