import logging
import math
import azure.functions as func

def Num_int(lower, upper, N):
    inte=0
    dx=(float(upper)-float(lower))/N
    for i in range(N):
        xi=float(lower)+(i+1/2)*dx
        inte+=abs(math.sin(xi))*dx
    return "  "+str(inte)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    para = req.params.get('name')
    if not para:
        try:
            req_body=req.get_json()
        except ValueError:
            pass
        else:
            para=req_body.get('name')

    if para:
        Nums = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
        interval=para.split("_")
        
        output=""
        for i in Nums:

            output+=Num_int(interval[0],interval[1], i)

        return func.HttpResponse(output)

    else:

        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
