print("Temperature Converter")

print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")

choice = int(input("Enter choice (1/2): "))

if choice == 1:
    c= float(input("Enter temperature in celsius: "))
    f= (c*9/5)+32
    print("Fahrenheit:",f)
    
elif choice == 2:
    f= float(input("Enter temperature in Fahrenheit:"))
    c= (f-32)*5/9
    print("Celsius:",c)
    
else:
    print("Invalid choice")