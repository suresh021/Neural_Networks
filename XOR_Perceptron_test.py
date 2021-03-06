import numpy as np


# sigmoid function
# activation function
def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))


# derivative of sigmoid function that
def sigmoid_der(x):
        return x*(1-x)


class NN:
    # default constructor
    # initialize weights
    def __init__(self, inputs = {}):
        self.inputs = inputs

        # learning rate
        self.alpha = 0.1

        # initialize weights w11,w12,w21,w22 with random values between -0.5 and 0.5
        # for i/p to hidden layer
        self.w11 = np.random.uniform(-.5,.5)
        # print("W11="+str(self.w11))
        self.w12 = np.random.uniform(-.5,.5)
        self.w21 = np.random.uniform(-.5, .5)
        self.w22 = np.random.uniform(-.5, .5)

        # initialize weight for bias
        self.wb1 = np.random.uniform(-.5, .5)
        self.wb2 = np.random.uniform(-.5, .5)

        # for hidden to o/p layer
        self.w1 = np.random.uniform(-.5, .5)
        self.w2 = np.random.uniform(-.5, .5)
        self.wb = np.random.uniform(-.5, .5)

        # hard code weights for testing
        self.w11 = .21
        self.w12 = -.4
        self.w21 = .15
        self.w22 = .1
        self.wb1 = -.3
        self.wb2 = .25
        self.w1 = -.2
        self.w2 = .3
        self.wb = -.4

    # training function
    def train(self, inputs, outputs, iterations):
        print("---------- Initial weights ----------")
        print("w11=" + str(self.w11) + "  w21=" + str(self.w21) + " w12=" + str(self.w12) + "  w22=" + str(self.w22))
        print("w1=" + str(self.w1) + "  w2=" + str(self.w2) + " wb1=" + str(self.wb1) + "  wb2=" + str(self.wb2))
        print("-------------------------------------\n")
        length_of_input = len(inputs) # i.e.  4
        for i in range(iterations):
            print("------------ITERATION:"+str(i)+"------------")
            print("For input: "+ str(inputs[i%length_of_input]))
            # s1 = x1 * w11 + x2*w21 + wb1*x3
            # l0[i%len(l0)] gives first array in iteration
            # for hidden layer
            s1 = np.dot(inputs[i%length_of_input],[self.w11,self.w21,self.wb1])
            s2 = np.dot(inputs[i%length_of_input], [self.w12, self.w22, self.wb2])
            # print("s1="+str(s1))
            # print("s2=" + str(s2))
            # find sigmoid functional value
            f1 = sigmoid(s1)
            print("f1=" + str(f1))

            f2 = sigmoid(s2)
            print("f2=" + str(f2))

            # for output layer
            s = np.dot([f1, f2, 1], [self.w1, self.w2, self.wb])
            # observed output for this iteration using feed forward
            f = sigmoid(s)
            print("f=" + str(f))

            # determining error (ie. Expected(f) - Observed(outputs[i%len(l0)]))
            expected_op = outputs[i%length_of_input]
            error_value = expected_op - f

            # terminate the loop if relative error is less than 0.1
            if abs(error_value)<=0.1:
                print("Expected accuracy obtained... exiting...")
                break

            # calculating error by multiplying with derivative
            # If the sigmoid functions gives you a HIGH or LOW value(Pretty good confidence),
            # the derivative of that value is LOW. If you get a value at the steepest slope(0.5),
            # the derivative of that value is HIGH.

            # When the function gives us a bad prediction,
            # we want to change our weights by a higher number,
            # and on the contrary, if the prediction is good(High confidence),
            # we do NOT want to change our weights much.
            delta_3 = error_value* sigmoid_der(f)
            print("Delta3 = " + str(delta_3))

            # determine weight corrections for output layer
            delta_w1 = delta_3 * self.alpha * f1
            delta_w2 = delta_3 * self.alpha * f2
            delta_wb = delta_3 * self.alpha * 1  # bias is 1


            # update weights at input layer

            delta_1 = delta_3*sigmoid_der(f1)*self.w1
            print("Delta1 = " + str(delta_1))
            delta_2 = delta_3*sigmoid_der(f2)*self.w2
            print("Delta2 = "+str(delta_2))

            # determine weight corrections for output layer
            delta_w11 = delta_1 * self.alpha * inputs[i%length_of_input][0] # x1
            delta_w12 = delta_2 * self.alpha * inputs[i%length_of_input][0]
            delta_w21 = delta_1 * self.alpha * inputs[i%length_of_input][1] #x2
            delta_w22 = delta_2 * self.alpha * inputs[i%length_of_input][1]
            delta_wb1 = delta_1 * self.alpha * inputs[i%length_of_input][2] #x3
            delta_wb2 = delta_2 * self.alpha * inputs[i%length_of_input][2] #x3

            # update all weights

            self.w11 = self.w11 + delta_w11
            self.w12 = self.w12 + delta_w12
            self.w21 = self.w21 + delta_w21
            self.w22 = self.w22 + delta_w22
            self.w11 = self.w11 + delta_w11
            self.w1 = self.w1 + delta_w1
            self.w2 = self.w2 + delta_w2
            self.wb1 = self.wb1 + delta_wb1
            self.wb2 = self.wb2 + delta_wb2
            self.wb = self.wb + delta_wb

            print("w11="+str(self.w11)+"  w21="+str(self.w21)+ " w12="+str(self.w12)+"  w22="+str(self.w22))
            print("w1="+str(self.w1)+"  w2="+str(self.w2)+ " wb1="+str(self.wb1)+"  wb2="+str(self.wb2))
            print("------------------------------------")


# [X1 X2 Bias]
inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

# Expected Output
outputs = np.array([ [0], [1], [1], [0]])

obj = NN(inputs)

obj.train(inputs,outputs, 100000)

