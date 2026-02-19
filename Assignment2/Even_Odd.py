# To print ODD or EVEN number taken from user

a = int(input("Enter the number to be verified: "))
print(f"{a} is an Even number") if a % 2 == 0 else print(f"{a} is an ODD number")