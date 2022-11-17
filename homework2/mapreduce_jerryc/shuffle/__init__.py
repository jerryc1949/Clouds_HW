# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

def main(words):
    word_count_list={}
    for i in words:
        for j in i:
            if j[0] not in word_count_list.keys():
                word_count_list[j[0]] = [1]
            else:
                word_count_list[j[0]].append(1)
    word_count_list=list(zip(word_count_list.keys(), word_count_list.values()))
    print(word_count_list)
    return word_count_list
