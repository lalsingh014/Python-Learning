while True:
    try:
        num = int(input("Enter positive number: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid ! Try Again.")