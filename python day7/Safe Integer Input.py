while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input!\nBro Enter an integer.")