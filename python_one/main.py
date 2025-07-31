import calc

while True:
  command = input("Enter a command (add, sub, mult, div) or 'stop' to exit: ")
  if command == 'stop':
    break
  
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue

  if command == 'add':
    result = calc.add(num1, num2)
    print(f"The result is: {result}")
  elif command == 'sub':
    result = calc.sub(num1, num2)
    print(f"The result is: {result}")
  elif command == 'mult':
    result = calc.mult(num1, num2)
    print(f"The result is: {result}")
  elif command == 'div':
    if num2 == 0:
      print("Error: Cannot divide by zero.")
    else:
      result = calc.div(num1, num2)
      print(f"The result is: {result}")
  else:
    print("Invalid command. Please try again.")