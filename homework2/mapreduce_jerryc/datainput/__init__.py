# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from azure.storage.blob import BlobServiceClient
def main(name:str) -> list:
    try:
        line_list = []
        nums=0
        print("Azure Blob Storage Python quickstart sample")
        AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=fengaoccount;AccountKey=Jf2NeThVt5imtdRobwdo3MTUw4gnRTaeDYzf0h1T0DQ/JDtPiiLVTCn0jgwZ++85RB9fwln7PRLU+ASterioXQ==;EndpointSuffix=core.windows.net"
        blob_service_client= BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_client=blob_service_client.get_container_client(container="mycontainer")
        blob_list = container_client.list_blobs()
        for i in blob_list:
            file = container_client.download_blob(i.name).readall()
            file = str(file, encoding='utf-8').split('\r\n')
            for j in file:
                line_list.append((num, j))
                nums+=1
        print(line_list)
    except Exception as ex:
        print('Exception:')
        print(ex)
    return line_list
