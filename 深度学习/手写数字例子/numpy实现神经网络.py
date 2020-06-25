
import numpy as np

class MLP_np:

    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))


    def dsigmod(z):
        return sigmoid(z)(1- sigmoid(z))

    def __init__(self,sizes):
        # sizes ：[784,30,10]
        # 784 到30的全连接
        self.sizes = sizes
        self.num_layers = len(sizes) - 1
        # sizes[:-1]  784,30    sizes[1:]   30,10
        self.weights = [np.random.randn(ch1,ch2) for ch1 ,ch2 in zip(sizes[:-1],sizes[1:])]
        self.biases = [np.random.randn(b) for b in sizes[1:]]
    def forward(self,x):
        # param: x [784,1]
        # return [10,1]
        for b,w in zip(self.biases,self.weights)
            [30,784]@[784,1]
            z = np.dot(w,x)+b
            x= sigmoid(z)
        return z

    def backward(self,x,y):
        # param  x: [784,1]
        # y:[10,1]
        # return
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        nabla_b = [np.zeros(b.shape) for w in self.biases]
        # 第一步  forward
        # 每一层保存激活
        activations = [x]
        # 每一层保存z
        zs =[]
        for b,w in zip(self.biases,self.weights):
            z = np.dot(w,x)+b
            activations = sigmoid(z)
            zs.append(z)
            activations.append(activations)
        # 第二部 backward
        # 完整例子.1 计算输出层和梯度
        # 输出层[10,1]
        delta = activations[-1]*(1-activations[-1])*(activations[-1]-y)
        nabla_b[-1] = delta
        # [10,1]@[1,30] =>[10,30]
        nabla_w[-1] = np.dot(delta, activations[-2].T)
        # 完整例子.完整例子 计算隐藏层
        for l in range(2,self.num_layers+1):
            l = -l
            z = zs[l]
            a = activations[l]
            # [10,30]T@[10,1] =>[30,1]
            delta = np.dot(self.weights[l+1].T,delta)*a*(1-a)

            nabla_b[l] = delta
            nabla_w[l] = np.dot(delta,activations[l-1].T)
        return nabla_w,nabla_b
    def train(self,training_data,epochs,batchsz,lr):
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            np.random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+batchsz]
                for k in range(0,n,batchsz):
                    self.update_mini_batch(mini_batch,lr)
                if test_data:
                    print("Epoch {0}:{1}/{2}".format(j,self.evaluate(test_data),n_test))
                else:
                    print("Epoch {0} complete:".format(j))
            ]







def main():












if __name__ == '__main__':
    main()
