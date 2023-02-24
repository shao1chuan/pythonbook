import optuna
import plotly
from optuna.visualization import plot_optimization_history
import numpy as np
import plotly.graph_objects as go

def himmelblau(x1, x2):
    # rosenbrock函数
    return ((x1**2) + x1 - 11)**2 + (x1 + x2 ** 2 - 7) ** 2

def df_himmelblau(x1, x2):
    return (x1 ** 2 + x1 - 11) *(4*x1+2) + (x1 + x2 ** 2 - 7) * 2, 2*(x1 + x2 **2 -7)*2*x2

def ddf_himmelblau(x1, x2):
    return 12*x1**2+12*x1+2,4*x1+12*x2**2-28

def rosenbrock(x1, x2):
    # rosenbrock函数
    return (1 - x1) ** 2 + 10 * (x2 - x1 ** 2) ** 2

def df_rosenbrock(x1, x2):
    return -2 + 2 * x1 - 40 * (x2 - x1 ** 2) * x1, 20 * (x2 - x1 ** 2)

def semicircle(x1, x2):
    # 半圆函数
    return x1 ** 2 + x2 ** 2

def df_semicircle(x1, x2):
    return x1 * 2 , x2 * 2

def semicircle2(x1, x2):
    return 0.1 * x1 ** 2 + 2 * x2 ** 2
def df_semicircle2(x1, x2):
    return x1 * 0.2 , x2 * 4



def plotF(fName,x,y,grid):
    x1 = np.arange(-x, x, grid)
    x2 = np.arange(-y, y, grid)
    x1, x2 = np.meshgrid(x1, x2)
    fig = go.Figure(data = [
        go.Surface(
        contours = {        "x": {"show": True, "start": -4, "end": 4, "size": 0.4, "color":"white"}, "y": {"show": True, "start": -4, "end": 4, "size": 0.4, "color":"white"}, "z": {"show": True, "start": 0.5, "end": 800, "size": 5}    },
        x = x1,
        y = x2,
        z = fName(x1,x2),
        opacity=0.2),
    ])
    fig.show()

def plotAll(fName,x1_history,x2_history):
    x1 = np.arange(-5, 5, 0.5)
    x2 = np.arange(-5, 5, 0.5)
    x1, x2 = np.meshgrid(x1, x2)
    z_history = eval(fName)(x1_history, x2_history)
    fig = go.Figure(data=[
        go.Surface(
            contours={"x": {"show": True, "start": -4, "end": 4, "size": 0.4, "color": "white"},
                      "y": {"show": True, "start": -4, "end": 4, "size": 0.4, "color": "white"},
                      "z": {"show": True, "start": 0.5, "end": 800, "size": 5}},
            x=x1,
            y=x2,
            z=eval(fName)(x1, x2),
            opacity=0.2),

        go.Scatter3d(
            x=x1_history, y=x2_history, z=z_history,
            mode='lines+markers',
            marker=dict(size=4, colorscale='Viridis', opacity=1),
            line=dict(width=2)
        ),

    ])
    fig.show()

def main():
    # plotF(rosenbrock,2,8,0.1)
    plotF(himmelblau, 5, 5, 0.5)
    # plotF(semicircle, 5, 5, 0.5)

if __name__ == '__main__':
    main()