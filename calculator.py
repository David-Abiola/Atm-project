ask = int(input("enter 1 for normal calculation and 2 for fraction "))
if ask == 1:
    print("welcome to the integer session")
    number_1 = float(input("number one "))
    number_2 = float(input("number two "))
    operation = input("enter operation ")
    if operation == "+":
        print(number_1 + number_2)
    elif operation == "-":
        print(number_1 - number_2)
    elif operation == "/":
        print(number_1 / number_2)
    elif operation == "*":
        print(number_1 * number_2)
elif ask == 2:
    from fractions import Fraction

    print("FRACTION CALCULATOR")
    print("Example input: 3/7 or 2/3")
    print()

    f1 = input("Enter first fraction: ")
    f2 = input("Enter second fraction: ")

    frac1 = Fraction(f1)
    frac2 = Fraction(f2)

    print("\nChoose operation:")
    print("Add (+)")
    print("Subtract (-)")
    print("Multiply (*)")
    print("Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "+":
        result = frac1 + frac2
    elif choice == "-":
        result = frac1 - frac2
    elif choice == "*":
        result = frac1 * frac2
    elif choice == "/":
        result = frac1 / frac2
    else:
        print("Invalid choice")
        exit()

    print("\nResult =", result)
    print("As mixed number =", result.numerator // result.denominator,
          "and", result.numerator % result.denominator, "/", result.denominator)
