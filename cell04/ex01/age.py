age = int(input("Please tell me your age : "))
age_F = 10

print("You are currently ",age," years old")

for i in range (3) :
    print("In ",age_F," years, you'll be ",str(age+10),"years old" )
    age_F += 10
    age += 10