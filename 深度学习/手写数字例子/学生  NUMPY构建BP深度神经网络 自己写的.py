import numpy  as np
import random
import mnist_loader

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))         #定义sigmoid函数

def dsigmoid(z):
    return sigmoid(z)(1-sigmoid(z))                                                   #定义sigmoid函数的导数


class MLP_np:
    def __init__(self,sizes):
        """
        size :[784,30,10]
        """
        self.sizes = sizes
        self.num_layers = len(sizes) - 1

        # sizes:[784,30,1]
        # w: [ch_out, ch_in]
        #biases: [ ch_out ]
        self.weights = [np.random.randn(ch2, ch1,)  for ch1, ch2 in zip(sizes[:-1], sizes[1:])]        #分别生成[784,30], [30,10]
        self.biases = [np.random.randn(ch, 1) for ch in sizes[1:]]


    def forward(self, x):                                                   #定义向后传递函数
            """
            x:[784,1]
            """
            for b,w in zip(self.biases, self.weights):
                #[30,784]@[784,1] =>[30,1]+[30,1]=>[30,1]
                z = np.dot(w, x) + b
                #[30,1]
                x = sigmoid(z)          #使用sigmoid函数来作为激活函数

            return x


    def backprop(self, x, y):                               #定义向前传递的函数
            """
            x:[784,1]
            y:[10,1]
            """
            nabla_w = [np.zeros(w.shape) for w in self.weights]
            nabla_b = [np.zeros(b.shape) for b in self.biases] 

            #1、 forward
            #save activations for every layer
            activarions = [x]
            #save z for every layer
            zs = []
            activation = x
            for b, w in zip(self.biases, self.weights):
                z = np.dot(w, activation) + b
                activation = sigmoid(z)
                zs.append(z)
                activarions.append(activation)

            loss = np.power(activarions[-1] - y, 2).sum()
            #完整例子、backward
            #完整例子.1、 compute gradient on output layer (在输出层计算梯度)
            #[10,1] with [10,1] => [10,1]
            delta = activarions[-1] * (1-activarions[-1]) * (activarions[-1] - y)
            nabla_b[-1] = delta
            # [10,1]@[1,30] =>[10,30]
            # activations:[30, 1]
            nabla_w[-1] = np.dot(delta, activarions[-2].T)         # activations.T是将activations矩阵转置

            #完整例子.完整例子 compute hidden gradient            (循环计算隐藏层梯度)
            for l in range(2, self.num_layers+1):
                l = -l

                z = zs[l]
                a = activarions[l]

                #delta_j
                #[10, 30]T @ [10, 1 ] => [30 ,10]@{10,1} => [30, 1] * [30, 1] =>[30, 1]
                delta = np.dot(self.weights[l+1].T, delta) * a * (1-a)

                nabla_b[l] = delta
                #[30, 1] @ [784, 1]T => [30, 784]
                nabla_w[l] = np.dot(delta, activarions[l-1].T)

            return nabla_w, nabla_b, loss




    def train(self, training_data, epochs, batchsz, lr, test_data):
        """
        training_data: list of (x,y)
        epochs: 1000
        vatchsz: 10
        lr: 0.01
        test_data: list of (x,y)
        """
        if test_data:
           n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                            training_data[k:k+batchsz]
                            for k in range(0, n, batchsz)]
            for mini_batch in mini_batches:
                loss = self.update_mini_batch(mini_batch, lr)


                if test_data:
                    print("Epoch {0}: {1} / {2}".format(
                        j, self.evaluate(test_data), n_test), loss)
                else:
                    print("Epoch {0} complete".format(j))

    def update_mini_batch(self, batch, lr):
        """
        batch: list of (x,y)
        lr = 0.01
        """
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        nabla_b = [np.zeros(b.shape) for b in self.biases] 
        loss = 0

        for x,y in batch:
            #list of every w/b gradient
            #[w1, w2, w3]
            nabla_w_, nabla_b_, loss_ = self.backprop(x, y)
            nabla_w = [accu+cur for accu, cur in zip(nabla_w, nabla_w_)]
            nabla_b = [accu+cur for accu, cur in zip(nabla_b, nabla_b_)] 
            loss += loss_

        nabla_w = [w/len(batch) for w in nabla_w]
        nabla_b = [b/len(batch) for b in nabla_b]
        loss =loss / len(batch)

        #w = w - lr * nabla_w
        self.weights = [w - lr * nabla for w, nabla in zip(self.weights, nabla_w)]
        self.biases = [b - lr * nabla for b, nabla in zip(self.biases, nabla_b)]

        return loss


    def evaluate(self, test_data):
        """
        test_data: list of (x,y)
        """
        result = [(np.argmax(self.forward(x)),y) for x,y in test_data]

        correct = sum(int(pred==y) for pred, y in result)

        return correct



def main():


    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    print(len(training_data), training_data[0][0].shape, training_data[0][1].shape)
    print(len(test_data), test_data[0][0].shape, test_data[0][1].shape)
    print(test_data[0][1])
    net = MLP_np([784, 30, 10])


    net.train(training_data, 1000, 10, 0.1, test_data=test_data)












if __name__=='__main__':
    main()