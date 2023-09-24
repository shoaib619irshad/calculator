add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b
fdiv = lambda a, b: a // b
mod = lambda a, b: a % b
exp = lambda a, b: a ** b


def cal(op, o1, o2):
    return op(o1, o2)


try:
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    task = int(input("Choose operation(1-7) to perform: \n1.SUM\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.FLOOR "
                     "DIVISION\n6.MODULUS\n7.EXPONENT\n"))
    match task:
        case 1:
            print("The result is: ", add(x, y))
        case 2:
            print("The result is: ", sub(x, y))
        case 3:
            print("The result is: ", mul(x, y))
        case 4:
            print("The result is: ", div(x, y))
        case 5:
            print("The result is: ", fdiv(x, y))
        case 6:
            print("The result is: ", mod(x, y))
        case 7:
            print("The result is: ", exp(x, y))
        case _:
            print("choose valid option")

except Exception as e:
    print(e)
    print("Enter numbers and operation correctly")
