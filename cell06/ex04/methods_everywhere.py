import sys

def enlarge(text):
    return text + 'z'

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) < 8:
            print(enlarge(arg))
        elif len(arg) == 8:
            print(arg)