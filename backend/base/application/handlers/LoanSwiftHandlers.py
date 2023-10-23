from ..commands.LoanSwiftCommands import CreateLoanSwiftCommand, DeleteLoanSwiftCommand, PatchLoanSwiftCommand
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
        raise Exception("handler", "The loan has not been accepted")
    
    return LoanSwiftRepository.save(command.data)


def PatchLoanSwiftHandler( command:PatchLoanSwiftCommand ):
    changes = dict(filter(lambda item: item[1] is not "" and item[1] is not None, command.clean().items()))
    if ( changes.__len__() <= 1 ):
        raise Exception("Handler", "No fields provided to change")
    
    loanSwiftSaved = LoanSwiftRepository.findById(command.data['id'])
    if (loanSwiftSaved.exists() == False):
        raise Exception("handler", "The loan does not currently exist")
    
    LoanSwiftRepository.patch(command.data)
    

def DeleteLoanSwiftHandler( command:DeleteLoanSwiftCommand ):
    loanSwiftSaved = LoanSwiftRepository.findById(command.data['id'])
    if (loanSwiftSaved.exists() == False):
        raise Exception("handler", "The loan does not currently exist")
    
    LoanSwiftRepository.delete(command.data['id'])

    
