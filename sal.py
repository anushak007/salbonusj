import sys

if len(sys.argv) == 2:
  sal = int(sys.argv[1])
  print("user input provided")
else:
  sal = 50000
  
bonus = sal + (sal * 10 / 100)

print("The salary is:", sal)
print("The updated salary is:", bonus)
