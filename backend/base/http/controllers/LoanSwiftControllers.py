from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from ..helpers.Response import sendSuccess, sendBadRequest, sendInternalError, sendCreated
from ...application.handlers.LoanSwiftHandlers import CreateLoanSwiftHandler, ListLoanSwiftHandler, DeleteLoanSwiftHandler, PatchLoanSwiftHandler
from ...application.commands.LoanSwiftCommands import CreateLoanSwiftCommand, DeleteLoanSwiftCommand, PatchLoanSwiftCommand

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listLoanSwift( request:Request ):
    try:
        payload = ListLoanSwiftHandler()
        
        return sendSuccess(payload)
    except Exception as ex:
        return sendInternalError(ex)


@api_view(["POST"])
def createLoanSwift( request:Request ):
    try:
        command = CreateLoanSwiftCommand( request.data )
        if (command.is_valid() == False):
            return sendBadRequest(command.errors)
        
        try:
            CreateLoanSwiftHandler(command)
        except Exception as ex:
            return sendBadRequest(ex.args[1])

        return sendCreated("Loan created successfully")
    except Exception as ex:
        return sendInternalError(ex)
    
    
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def patchLoanSwift( request:Request, id:str ):
    try:
        request.data['id'] = id
        command = PatchLoanSwiftCommand(request.data)
        if (command.is_valid() == False):
            return sendBadRequest(command.errors)

        try:
            PatchLoanSwiftHandler(command)
        except Exception as ex:
            return sendBadRequest(ex.args[1])
            
        return sendSuccess("The loan has been edited satisfactorily")
    except Exception as ex:
        return sendInternalError(ex)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteLoanSwift( request:Request, id:str ):
    try:
        command = DeleteLoanSwiftCommand({ 'id': id })
        if (command.is_valid() == False):
            return sendBadRequest(command.errors)

        try:
            DeleteLoanSwiftHandler(command)
        except Exception as ex:
            return sendBadRequest(ex.args[1])

        return sendSuccess("Loan successfully eliminated")
    except Exception as ex:
        return sendInternalError(ex)