import logging
import json
import azure.functions as func
from  .SESAME3_Exec import keycontrol as SESAME

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    bodydata = req.get_body().decode()
    
    if not bodydata:
        return func.HttpResponse(
            "requied body data!",
            status_code=400
        )

    if bodydata:
        try:
            logging.info(f"Body JSON: {req.get_json()}")
            bodyjson=req.get_json()
        except ValueError:
            pass
        #print(bodydata)
        #print(json.loads(bodydata))

        rtn=SESAME(bodyjson['uuid'],bodyjson['sk'],bodyjson['api_key'],bodyjson['cmd'],bodyjson['history'])

        return func.HttpResponse(rtn)
        #return func.HttpResponse(bodydata)






#    if not name:
#        try:
#            #print(req,get_json())
#            rtn1="test"
#            req_body = req.get_json()
#        except ValueError:
#            pass
#        else:
#            name = req_body.get('name')

#    if name:
#        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#    else:
#        return func.HttpResponse(
#             #req_body,
#             name,
#             status_code=200
#        )
