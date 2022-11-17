# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
import logging
import azure.durable_functions as df
import azure.functions as func

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    cli = df.DurableOrchestrationClient(starter)
    in_id = await client.start_new(req.route_params["functionName"], None, None)
    logging.info(f"Started orchestration with ID = '{in_id}'.")
    return cli.create_check_status_response(req, in_id)
