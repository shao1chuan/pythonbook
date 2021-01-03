# https://blog.csdn.net/qq_37236745/article/details/103698507
import numpy as np
# compute loss
def compute_error(b, w, points):
    totalError = 0
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (w * x + b)) ** 2
    return totalError / float(len(points)) # average

# compute gradient
def step_gradient(b_current, w_current, points, learningRate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(points))
    for i in range(len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += 2 * ((w_current * x) + b_current - y)
        w_gradient += 2 * x * ((w_current * x) + b_current - y)
    b_gradient = b_gradient / N
    w_gradient = w_gradient / N
    new_b = b_current - (learningRate * b_gradient)
    new_w = w_current - (learningRate * w_gradient)
    return [new_b, new_w]

def gradient_descent_runner(points, starting_b, starting_w, learning_rate, num_iterations): # num_iteration 迭代次数
    b = starting_b
    w = starting_w
    error = np.zeros(num_iterations)
    for i in range(num_iterations):
        b, w = step_gradient(b, w, np.array(points), learning_rate)
        error[i] = compute_error(b, w, points)
    return [b, w],error

def run():
    points = np.genfromtxt("data.txt", delimiter=",")
    learning_rate = 0.000001
    initial_b = np.random.random()
    initial_w = np.random.random()
    num_iterations = 1000
    print("Starting gradient descent at b = {0}, w = {1}, error = {2}"
          .format(initial_b, initial_w,
                  compute_error(initial_b, initial_w, points)))
    print("Running...")
    [b, w],error = gradient_descent_runner(points, initial_b, initial_w, learning_rate, num_iterations)
    print("After {0} iterations at b = {1}, w = {2}, error = {3}"
          .format(num_iterations, b, w,
                  compute_error(b, w, points)))

    import matplotlib.pyplot as plt
    fig, bx = plt.subplots(figsize=(8, 6))
    bx.plot(np.arange(num_iterations), error, 'r')
    bx.set_xlabel('Iterations')
    bx.set_ylabel('Cost')
    bx.set_title('Error vs. Training Epoch')
    plt.show()
run()