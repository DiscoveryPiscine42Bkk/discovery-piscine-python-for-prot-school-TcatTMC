import sys

# print(sys.argv)

if len(sys.argv) != 2 :
    print(sys.argv)
    print("none")

else :
    
    word = input("What was the parameter? : ")

    if word == sys.argv[1] :
        print("Good job!")

    else :
        print("Nope, sorry...")