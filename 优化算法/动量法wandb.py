import numpy as np
from function import *
import wandb
import math

z_history = []
x1_history = []
x2_history = []
# fName = 'semicircle'
# fName =  'rosenbrock'
fName = 'semicircle2'
fName =  'himmelblau'
dfName = 'df_'+fName
def objective():
    x1 = 0.1
    x2 = 0.1
    lr = 0.01
    # x1 = trial.suggest_float("x1", 0, 3)
    # x2 = trial.suggest_float("x2", 0, 3)
    beta = 0.5
    # lr = trial.suggest_float("lr", 0, 0.1)
    epochs = 15

    z = eval(fName)(x1, x2)
    z_history.append(z)

    v1,v2 = 0,0
    for epoch in range(epochs):
        dx1, dx2 = eval(dfName)(x1, x2)
        v1 = beta * v1 + (1-beta)* dx1
        v2 = beta * v2 + (1-beta) * dx2

        x1 -= lr * v1
        x2 -= lr * v2

        x1_history.append(x1)
        x2_history.append(x2)
        z = eval(fName)(x1, x2)
        z_history.append(z)
        wandb.log({
            'loss': z,
        })

    return eval(fName)(x1, x2)

def RMS():
    x1 = 0.1
    x2 = 0.1
    lr = 0.2
    # x1 = trial.suggest_float("x1", 0, 3)
    # x2 = trial.suggest_float("x2", 0, 3)
    beta = 0.5
    # lr = trial.suggest_float("lr", 0, 0.1)
    epochs = 15

    z = eval(fName)(x1, x2)
    z_history.append(z)

    s1 ,s2 = 0,0
    for epoch in range(epochs):

        dx1, dx2 = eval(dfName)(x1, x2)

        s1 = beta*s1+(1-beta)* dx1 ** 2
        s2 = beta*s2+(1-beta)* dx2 ** 2

        lr1,lr2 = lr/ math.sqrt(s1),lr/ math.sqrt(s2)
        x1 -= lr1  * dx1
        x2 -= lr2  * dx2

        x1_history.append(x1)
        x2_history.append(x2)
        z = eval(fName)(x1, x2)
        z_history.append(z)
        wandb.log({
            'loss': z,
        })
    return eval(fName)(x1, x2)

def main():
    RMS()
    plotAll(fName,np.array(x1_history), np.array(x2_history))



if __name__ == '__main__':
    wandb.init(project="优化算法", name="RMS")
    main()
    wandb.finish()