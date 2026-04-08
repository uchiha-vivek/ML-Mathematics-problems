# f(x) = x^2
# f'(x) = 2x

# calcualating gradient decent


##--------------------Method 1------------------------##

# def gradient_decent(lr=0.1, iterations=25):
#     x = 5
#     for i in range(iterations):
#         grad= 2*x
#         x = x - lr*grad
#         print(f"Step {i+1} : x = {x:.4f}")
#     return x


##--------------------Method 2 ------------------------##
def gradient_decent(iterations:int, learning_rate:int, init:int)-> float:
    minimize = init
    for _ in range(iterations):
        derivative = 2 * minimize
        minimize = minimize - learning_rate * derivative
    return round(minimize,4)


    
if __name__=="__main__":
    # gradient_decent()
    ans = gradient_decent(25,0.1,5)
    print(ans)