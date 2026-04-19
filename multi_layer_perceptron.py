import numpy as np


class MLP:

    def __init__(self):

        # Input -> Hidden
        self.W1 = np.random.randn(
            2,2
        )

        self.b1 = np.zeros(
            (2,)
        )


        # Hidden -> Output
        self.W2 = np.random.randn(
            2
        )

        self.b2 = 0.0


    # -----------------
    # Activation
    # -----------------

    def sigmoid(self,z):

        return 1/(1+np.exp(-z))


    def sigmoid_derivative(self,a):

        return a*(1-a)


    # -----------------
    # Forward Pass
    # -----------------

    def forward(self,x):

        # Hidden layer

        self.z1=np.dot(
            self.W1,
            x
        ) + self.b1

        self.a1=self.sigmoid(
            self.z1
        )


        # Output layer

        self.z2=np.dot(
            self.W2,
            self.a1
        ) + self.b2

        self.y_hat=self.sigmoid(
            self.z2
        )

        return self.y_hat


    # -----------------
    # Backprop
    # -----------------

    def backward(self,x,y):

        y_pred=self.forward(x)


        # Output layer error

        delta2=(
            y_pred-y
        ) * self.sigmoid_derivative(
            y_pred
        )


        dW2=delta2*self.a1

        db2=delta2


        # Hidden layer error

        delta1=(
            self.W2*delta2
        ) * self.sigmoid_derivative(
            self.a1
        )


        dW1=np.outer(
            delta1,
            x
        )

        db1=delta1


        return (
            dW1,
            db1,
            dW2,
            db2
        )


    # -----------------
    # Gradient Descent
    # -----------------

    def train(
        self,
        x,
        y,
        lr=0.1,
        epochs=1000
    ):

        for i in range(epochs):

            dW1,db1,dW2,db2 = \
            self.backward(
                x,y
            )


            # Update weights

            self.W1 -= lr*dW1

            self.b1 -= lr*db1

            self.W2 -= lr*dW2

            self.b2 -= lr*db2


            if i%100==0:

                pred=self.forward(x)

                loss=0.5*(
                    pred-y
                )**2

                print(
                    f"Epoch {i}, Loss={loss}"
                )


if __name__=="__main__":
    x=np.array([
1.0,
2.0
])

y=1.0


model=MLP()

model.train(
    x,
    y,
    lr=0.1,
    epochs=1000
)


print(
"\nFinal Prediction:",
model.forward(x)
)
