import sys
z = len(list(sys.argv[1]))
i = 0
while i < z:
    if 'z' in (sys.argv[1])[i]:
        print('z',end='')
    i += 1