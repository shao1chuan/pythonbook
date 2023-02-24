import numpy as np
from function import *

z_history = []
x1_history = []
x2_history = []
# fName = 'semicircle'
# fName =  'rosenbrock'
fName = 'semicircle2'
fName =  'himmelblau'
dfName = 'df_'+fName
def objective(trial):
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

    return eval(fName)(x1, x2)

def main():
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=1, timeout=600)
    plot_optimization_history(study).show()
    plotAll(fName,np.array(x1_history), np.array(x2_history))
    print(study.best_value,study.best_trial)



if __name__ == '__main__':
    main()