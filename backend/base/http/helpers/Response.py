from rest_framework.response import Response
from rest_framework import status

def sendSuccess(payload = {}):
    """
    Receives a payload and returns an HttpResponse status 200 with the payload

    args:
        payload [dict]: Payload to response

    return:
        response: {
            payload [dict],
        }
    """

    try:
        return Response({
            'payload': payload
        }, status=status.HTTP_200_OK )
    except Exception as ex:
        return


def sendBadRequest( payload ):
    """
    Receives a payload and returns an HttpResponse status 400 with the payload

    args:
        payload [dict]: Payload to response

    return:
        response: {
            payload [dict],
        }
    """
    return Response({
        'payload': payload
    }, status=status.HTTP_400_BAD_REQUEST)


def sendCreated( payload ):
    """
    Receives a payload and returns an HttpResponse status 201 with the payload

    args:
        payload [dict]: Payload to response

    return:
        response: {
            payload [dict],
        }
    """
    return Response({
        'payload': payload
    }, status=status.HTTP_201_CREATED)


def sendInternalError( ex:Exception ):
    """
    Receives an exception and returns a http status 500 response with the trace of error
    
    args:
        ex [ exception ]: System exception object

    return:
        response: {
            status: 'error',
            message: 'Internal Server Error [500]',
            trace: [ Array object ]
        } 
    """

    data = {
        'status': 'error',
        'message': 'Internal Server Error [500]',
        'trace': ex.args
    }
    return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)