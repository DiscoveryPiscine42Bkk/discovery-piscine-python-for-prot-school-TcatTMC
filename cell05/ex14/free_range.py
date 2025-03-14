import sys
if len(sys.argv) == 3:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    array = []
    i = 1
    array.append(start)
    while i < abs(start-stop):
        if start<stop:
            array.append(start+i)
        if start>stop:
            array.append(start-i)
        i += 1
    array.append(stop)
    array = list(dict.fromkeys(array))
    print(array)
else:
    print('none')