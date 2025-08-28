#Calculator

try:
  num1=int(input("Enter 1st number:"))
  num2=int(input("Enter 2nd number:"))
  operation=input("Enter the operation (+,-,/,*,%):")
  match operation:
    case '+':
      print(f"The sum of {num1} and {num2}: {num1+num2}")
    case '-':
      print(f"The sub of {num1} and {num2}: {num1-num2}")
    case '*':
      print(f"The mul of {num1} and {num2}: {num1*num2}")
    case '/':
      print(f"The div of {num1} and {num2}: {num1/num2}")
    case '%':
      print(f"The modules of {num1} and {num2}: {num1%num2}")
    case default:
      print("Invalid operation")
except Exception as e:
  print("Invalid entry.",e)