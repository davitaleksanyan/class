def leap_year(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
        print("year is a leap")
    else:
        print("year is not a leap")
leap_year(2300)

def triangle(a, b, c):
    if a ==0 or b ==0 or c ==0:
        print("it is not a triangle")
    elif a+b<c or a+c<b or c+b<a:
         print("it is not a triangle")
    elif a==b==c:
        print("simple triangle")
    elif a==b or a==c or c==b:
        print("isosceles triangle")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
        print("square triangle")
    else:
        print("triangle with such sides does not exist")
triangle(1,2,5)

def runner(x, y):
    i = 0
    while x<=y:
        x *= 1.1
        i +=1
    print(i)
runner(10, 50)

def chess(x, y, x1, y1):
    if abs(x-x1)==1 and abs(y - y1)==1:
        print("ok")
    elif x==x1 and abs(y - y1)==1:
        print("ok")
    elif y == y1 and abs(x - x1) == 1:
        print("ok")
    else:
        print("BOOOM")

chess(8,8,5,6)

