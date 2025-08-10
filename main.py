#day 10
#projet day 10 calculator

#add
def add(n1,n2):
  return n1+n2
#Subtract
def sub(n1,n2):
  return n1-n2
#Multiply
def mul(n1,n2):
  return n1*n2
#Divide
def div(n1,n2):
  return n1/n2

operation = {

"+": add,
"-": sub,
"*": mul,
"/": div

}
def calculator():
 
  print (''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|      
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ''')
   
  print ("\n")

  print ("Welcome to the calcultor program!")
  num1 = float (input("what is the first number ? "))
  question = True
  while True:
    
      for symbol in operation :
        print (symbol)
      
      operation_symbol = input("Pick an operation from the line above :  ")
      num2 = float (input("what is the next number ? "))
      if operation_symbol == "+":
        answer = add (num1, num2)
      if operation_symbol == "-":
        answer = sub (num1, num2)
      if operation_symbol == "*":
        answer = mul (num1, num2)
      if operation_symbol == "/":
        answer = div (num1, num2)
      
      print (f"{num1} {operation_symbol} {num2} = {answer}")
      
      question = input (f"Type 'y' if you want to continue calculating with {answer} , or type 'n' to start a new calculation :")
      if question == "y":
        num1 = answer
        continue
      else:
        question = False
        calculator ()

calculator ()