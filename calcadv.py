num1=float(input("Enter a number:"))
op=input("Enter operater:")
num2=float(input("Enter a number:"))
def cal(op,num1,num2):
    if op=="+":
        num=(num1+num2)
    elif op=="-":
        num=(num1-num2)
    elif op=="*":
        num=(num1*num2)
    elif op=="/":
        num=(num1/num2)
    elif op=="%":
        num=(num1%num2)
    else:
        print("NOT A VALID OPERATION") 
        return 0      
    return num    
num=cal(op,num1,num2)
if num==0:
    print("Sorry")
else:
    print("RESULT:",num)

   
        


      