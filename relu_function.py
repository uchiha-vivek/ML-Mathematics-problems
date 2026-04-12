## coding relu function

def relu(x:int)-> int :
    return max(0,x)
    
    
if __name__=="__main__":
    ans1 = relu(2)
    ans2 = relu(-2)
    print(ans1,ans2)