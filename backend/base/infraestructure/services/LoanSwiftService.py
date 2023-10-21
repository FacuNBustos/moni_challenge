import requests

def AcceptanceConsultation( document_number:int ) -> bool:
    """
    Receives an ID and wonders if he can receive a loan

    args:
        document_number [int]: ID to verify loan possibility

    return:
        response [boolean]: True | False
    """

    try:
        response = requests.get( r'https://api.moni.com.ar/api/v4/scoring/pre-score/{0}'.format(document_number), headers={
            'Content-Type': 'application/json',
            'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u',
        }, timeout=3000 )

        if ( response.status_code == 200 and response.json()['status'] == 'approve' ):
            return True
        
        return False
    except Exception as ex:
        return False