num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Prime check
if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(i,"Divides:",num)
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("so",num,"is Not prime")
