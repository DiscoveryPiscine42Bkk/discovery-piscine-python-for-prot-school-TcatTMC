import sys

def greetings(name=None):
    if isinstance(name,str):
        print('Hello,',name+'.')
    elif name == None:
        print('Hello, noble stranger.')
    else:
        print('Error: It was not a name.')

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)