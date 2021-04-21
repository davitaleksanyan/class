line = 1
for lin in range(5):
    print(line, 0, lin)
    line += 1
def isPalindrome(string):
        left_pos = 0
        right_pos = len(string) - 1
        while right_pos >= left_pos:
            if not string[left_pos] == string[right_pos]:
                return False
            left_pos += 1
            right_pos -= 1
        return True
print(isPalindrome('davit'))

def area(a):
    pi = 3.14
    s = pi*(a**2)
    print(s)
r = 2
area(r)

def show_employee_basic_data(name, age):
    print(name, "is a", age)
name = "Davit"
show_employee_basic_data(name, 38)

def  show_employee(name, salary = 9000):
    print("Salary of a ", name, "is a ", salary)
show_employee("Davit", 150000)

def show_whole_employee_info():
    print(how_employee_basic_data(name, age), "and", show_employee(name, salary = 9000) )
show_whole_employee_info(show_employee_basic_data(name, 38), show_employee("Davit", 1800000))


