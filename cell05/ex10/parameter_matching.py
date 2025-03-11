def para (pa_w):
    
    if num_pa != 1 :
        print("none")

    else :

        word = input(" What was the parameter? : ")
        if word == pa_w :
            print("Good job!")

        else :
            print("Nope, sorry...")


num_pa = para.__code__.co_argcount



para('Hello')