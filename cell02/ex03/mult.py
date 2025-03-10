number1 = int(input("please enter First number : "))
number2 = int(input("please enter second number : "))

print(str(number1)+" "+"x"+" "+str(number2)+" "+"="+" "+str(number1*number2) )

if number1*number2 < 0 :
    print("The result is negative.")

elif number1*number2 > 0 :
    print("The result is positive.")

elif number1*number2 == 0 :
    print("The result is positive and negative.")