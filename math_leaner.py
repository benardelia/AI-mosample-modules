# simple implementation of neural network to learn math
# the program will teach a computer 
# to predict output of mathematics expression without knowing the exact formula

from numpy import exp, array, random, dot

class neural_network:
    def __init__(self):
        # seed(1) ensure sequence of produced random number is the same each time 
        random.seed(1)
        # module have two inputs and one output
        self.weight = 2 * random.random((2, 1)) - 1

    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01 * dot(inputs.T, error)
            self.weight += adjustment
           

    def think(self, inputs):
        return (dot(inputs, self.weight))


neural_net = neural_network()

inputs = array([[2, 4], [1, 3], [3, 5]])
outputs = array([[16, 11, 21]]).T

# model will test 10000 times then it will come with the most possible answer
neural_net.train(inputs, outputs, 10000)

print(round(neural_net.think(array([125, 112]))[0]))
