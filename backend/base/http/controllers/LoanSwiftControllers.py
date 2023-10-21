from rest_framework.decorators import api_view
from rest_framework.request import Request
from ..helpers.Response import sendSuccess, sendBadRequest, sendInternalError, sendCreated
from ...application.handlers.LoanSwiftHandlers import CreateLoanSwiftHandler, ListLoanSwiftHandler
from ...application.commands.LoanSwiftCommands import CreateLoanSwiftCommand

@api_view(["GET"])
def listLoanSwift( request:Request ):
    payload = ListLoanSwiftHandler()
    return sendSuccess(payload)

@api_view(["POST"])
def createLoanSwift( request:Request ):
    try:
        command = CreateLoanSwiftCommand( request.data )
        if (command.is_valid() == False):
            return sendBadRequest(command.errors)
        
        try:
            CreateLoanSwiftHandler(command)
        except Exception as ex:
            return sendBadRequest(ex.args)

        return sendCreated("Ok")
    except Exception as ex:
        return sendInternalError(ex)