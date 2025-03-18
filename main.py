# Calc

print("""
########
# CALC #
########
""")

while True:
    x = float(input("x: "))
    y = float(input("y: "))
    select = input("Select (+-*/): ")

    if select == "+":
        print(f"{x} + {y} =", x + y)
    elif select == "-":
        print(f"{x} - {y} =", x - y)
    elif select == "*":
        print(f"{x} * {y} =", x * y)
    elif select == "/":
        print(f"{x} / {y} =", x / y)
    else:
        print("Error!")