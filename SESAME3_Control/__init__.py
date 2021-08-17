import logging
import json
import azure.functions as func
from  .SESAME3_Exec import keycontrol as SESAME

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    bodydata = req.get_body().decode()
    header_uuid = req.headers.get('uuid')
    header_sk = req.headers.get('sk')
    header_api_key = req.headers.get('api-key')
    
    if not bodydata:
        return func.HttpResponse(
            "requied body data!",
            status_code=400
        )
    
    if not header_uuid:
        return func.HttpResponse(
            "requied header uuid",
            status_code=400
        )
    
    if not header_sk:
        return func.HttpResponse(
            "requied header sk",
            status_code=400
        )
    
    if not header_api_key:
        return func.HttpResponse(
            "requied header api-key",
            status_code=400
        )

    if bodydata:
        try:
            logging.info(f"Body JSON: {req.get_json()}")
            bodyjson=req.get_json()
        except ValueError:
            pass

        rtn=SESAME(header_uuid,header_sk,header_api_key,bodyjson['cmd'],bodyjson['history'])

        return func.HttpResponse(rtn)
        #return func.HttpResponse(bodydata)
