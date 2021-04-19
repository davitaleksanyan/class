'''
number = int(input("Enter number :"))
def digits(n):
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i
exp = 10**(digits(number)-1)
while number > 0:
    each_digit  = number // exp
    number %= exp
    exp = int(exp/10)
    print (each_digit)


name = input("Enter some text :")
number_of_characters = len(name)
print("There are", number_of_characters, "symbols")

num = int(input("Enter number :"))
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
        print(num, "is not a prime number")

for line in range(6):
    print(line , "00000")

'''
total = 0
for x in range(0, 14, 1):
    total = total + x
    print(total)





