while True:
    try:
        a = int(input("A: "))
        b = int(input("B: "))
        print("Result:", a/b)
        break
    except ZeroDivisionError:
        print("Cannot divide by zero. Try Again.")
    except ValueError:
        print("Enetr valid integers. Try Again.")