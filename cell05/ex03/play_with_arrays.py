o_num = [2, 8, 9, 48, 8, 22, -12, 2]
n_num = [ x + 2 for x in o_num if x > 5 ]

c_num = list(set(n_num))

print(o_num)
print(c_num)