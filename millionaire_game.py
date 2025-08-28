#Who wants to be a millionaire
while True:
  ask=input("Would you like to play the game? (yes or no):\n")
  if ask.lower()=="yes":
    print("Lets start...")
    break
  elif ask.lower()=="no":
    print("OK Bye.")
    quit()
  else:
    print("Invalid input")
    
point=0
questions=[
  ["Who is Prabhas?", "Teacher", "Actor", "CEO", "Engineer", 2],
  ["What is a cat?", "Animal", "Human", "Ghost", "Non-living thing", 1],
  ["What is an apple?", "Dry-fruit", "Animal", "Vegetable", "Fruit", 4],
  ["When is Christmas Day celebrated?", "November", "January", "December", "April", 3]
]

for question in questions:
  print("\n",question[0],sep="")
  print("Option 1:",question[1])
  print("Option 2:",question[2])
  print("Option 3:",question[3])
  print("Option 4:",question[4])
  x=int(input("Enter the correct option:"))
  if(x==question[5]):
    point+=1
    print("Correct answer")
  else:
    print("Wrong answer")
  continue

print("\nResult:")
if (point==1):
  print(f"You got {point} point")
else:
  print(f"You got {point} points")