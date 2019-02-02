#ENTRY IS ALWAYS IN FORM OF STRING
num1=input("Enter a number:")
num2=input("Enter a number:")
add=float(num1)+float(num2)#TYPE CASTING
if float(num1)>=float(num2):
    diff=float(num1)-float(num2)
else:
    diff=float(num2)-float(num1)
mult=float(num1)*float(num2)
div=float(num1)/float(num2)
rem=float(num1)%float(num2)
print("Sum:",add)
print("Diffrence:",diff)
print("Product:",mult)
print("Quotent:",div)
print("Remainder:",rem)


