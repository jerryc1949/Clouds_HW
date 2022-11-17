import math
from flask import Flask

app=Flask(__name__)


def Num_Int(lower, upper, N):
    inte=0
    dx=(float(upper)-float(lower))/N
    for i in range(N):
        xi=float(lower)+(i+1/2)*dx
        inte+=abs(math.sin(xi))*dx
    return inte


@app.route('/<lower>/<upper>', methods=['GET'])
def get_numerical_integration(lower, upper):
    N=[10, 100, 1000, 10000, 100000, 1000000, 10000000]
    output={'res':[]}
    for i in N:
        output['res'].append(Num_Int(lower, upper, i))
    status_code=200
    return output, status_code



