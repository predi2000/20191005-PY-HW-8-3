x=int(input("Please enter Value 1: "))
y=int(input("Please enter Value 2: "))
calc_op=input("Please choose calc operation +, -, *, /: ")

if calc_op == "+":
    print(x + y)
elif calc_op == "-":
    print(x - y)
elif calc_op == "*":
    print(x * y)
elif calc_op == "/":
    print(x / y)
else:
    print("Sorry, wrong operation. Try again.")