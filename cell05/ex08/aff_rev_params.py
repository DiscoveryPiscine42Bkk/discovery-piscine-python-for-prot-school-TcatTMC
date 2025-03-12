import sys

if len(sys.argv) < 3 :
    print("none")

else : 
    for info in list(reversed(sys.argv[1:])):
        print(info)