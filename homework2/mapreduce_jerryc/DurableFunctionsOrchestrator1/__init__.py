# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt


import azure.functions as func
import azure.durable_functions as df

def orche_func(context: df.DurableOrchestrationContext):
    lines = yield context.call_activity("datainput", "")
    map_list=[]
    for i in lines:
        map_list.append(context.call_activity("map", i))
    word=yield context.task_all(map_list)
    words_count=yield context.call_activity("shuffle", word)
    reduce_list=[]
    for i in words_count:
        reduce_task.append(context.call_activity("reduce", i)) 
    result = yield context.task_all(reduce_list)
    print(result)
    return result
main = df.Orchestrator.create(orche_func)
