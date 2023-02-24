import numpy as np
from function import *
z_history = []
x1_history = []
x2_history = []
# fName = 'semicircle'
# fName =  'rosenbrock'
# fName = 'semicircle2'
fName =  'himmelblau'
dfName = 'df_'+fName
ddfName = 'ddf_'+fName
def objective(trial):
    x1 = 0.1
    x2 = 0.1
    epochs = 15
    z = eval(fName)(x1, x2)
    z_history.append(z)

    for epoch in range(epochs):
        alpha = pow(1.2, -epoch) * 20
        dx1, dx2 = eval(dfName)(x1, x2)
        ddx1,ddx2 = eval(ddfName)(x1, x2)

        x1 -= dx1/(alpha+ddx1)
        x2 -= dx2/(alpha+ddx2)

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