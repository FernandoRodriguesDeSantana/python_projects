# functions:
def sum_number(x,y):
  return x + y

def subtration_number(x,y):
  return x - y

def multiplication_number(x,y):
  return x * y

def division_number(x,y):
  return x / y

choice = int(input("1.Sum\n2.Subtration\n3.Multiplication\n4.Division\n"))

if choice in (1,2,3,4):
  number1 = float(input("\nEnter the first number: "))
  number2 = float(input("\nEnter the second number: "))

  if choice == 1:
    result = sum_number(number1,number2)
    print(f"\nResult = {result}")
  elif choice == 2:
    result =subtration_number(number1,number2)
    print(f"\nResult = {result}")
  
  elif choice == 3:
    result = multiplication_number(number1,number2)
    print(f"\nResult = {result}")
  
  elif choice == 4:
    result = division_number(number1,number2)
    print(f"\nResult = {result}")

  else:
    print("\nWrong option")
