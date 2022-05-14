# Modules
import os
import math

# Set degree as default
global defaultUnit
currentUnit = 'DEGREE'

# FUNCTIONS

def getCalcOperation():
  # Calculator program
  global operation
  operation = ''
  print('\nADDITION | SUBTRACTION | MULTIPLICATION | DIVISION | EXPONENTIATION | MODULO | FLOOR DIVISION | SQUARE ROOT | X ROOT | SINE | COSINE | TANGENT | LOGARITHM | FACTORIAL | MODE')
  while operation not in ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'EXPONENTIATION', 'MODULO', 'FLOOR DIVISION', 'SQUARE ROOT', 'X ROOT', 'SINE', 'COSINE', 'TANGENT', 'LOGARITHM', 'FACTORIAL', 'MODE']:
    print('Select an operation:')
    operation = input().upper()

def setOperationSymbol():
  os.system('clear')
  global operationSymbol
  if operation == 'ADDITION':
    operationSymbol = '+'
  elif operation == 'SUBTRACTION':
    operationSymbol = '-'
  elif operation == 'MULTIPLICATION':
    operationSymbol = 'x'
  elif operation == 'DIVISION':
    operationSymbol = '÷'
  elif operation == 'EXPONENTIATION':
    operationSymbol = '^'
  elif operation == 'MODULO':
    operationSymbol = '%'
  elif operation == 'FLOOR DIVISION':
    operationSymbol = '//'
  elif operation == 'SQUARE ROOT':
    operationSymbol = '√'
  elif operation == 'X ROOT':
    operationSymbol = '√'
  elif operation == 'SINE':
    operationSymbol = 'sin'
  elif operation == 'COSINE':
    operationSymbol = 'cos'
  elif operation == 'TANGENT':
    operationSymbol = 'tan'
  elif operation == 'LOGARITHM':
    operationSymbol = 'log'
  elif operation == 'FACTORIAL':
    operationSymbol = '!'

  # User wants to change mode between radians and degree
  if operation == 'MODE':
    global trigUnit
    trigUnit = ''
    while trigUnit not in ['DEGREE', 'RADIAN']:
      print('DEGREE or RADIAN mode?')
      trigUnit = input().upper()
    
    global currentUnit
    currentUnit = trigUnit
    
    os.system('clear')
    print('C A L C U L A T O R    ({0})' .format(trigUnit))

    getCalcOperation()
    setOperationSymbol()


def getCalcInput():
  global value1
  global value2

  # If the operation requires only 1 value, only ask for 1 value
  if operation == 'SQUARE ROOT':
    print('Enter value: ')
    while True:
      try:
        print('{0} '.format(operationSymbol), end=' ')
        value1 = float(input())
        break # Break if the value is a float
      except ValueError:
        print('Please enter a single numerical value.')

  # Degree/Radians must be considered for trig ratios
  elif operation in ['SINE', 'COSINE', 'TANGENT']:
    print('Enter value: ')
    while True:
      try:
        print('{0} '.format(operationSymbol), end=' ')
        value1 = float(input())
        break # Break if the value is a float
      except ValueError:
        print('Please enter a single numerical value.')
    if trigUnit == 'RADIANS':
      value1 = math.radians(value1)
    
  # Factorial has the operationSymbol after the value1
  elif operation == 'FACTORIAL':
    print('Enter value: ')
    while True:
      try:
        value1 = float(input())
        os.system('clear')
        break # Break if the value is a float
      except ValueError:
        print('Please enter a single numerical value.')
    # Clear and print this again so it puts the factorial symbol after the input
    print('Enter value:') 
    print(value1, operationSymbol)
  # The rest of the operations require 2 values, so ask for 2 values

  else:
    print('Enter first value:')
    while True:
      try:
        value1 = float(input())
        break # Break if the value is a float
      except ValueError:
        print('Please enter a single numerical value.')
    print('Enter second value:')
    while True:
      try:
        global value2
        print(value1, operationSymbol, end=' ')
        value2 = float(input())
        break # Break if the value is a float
      except ValueError:
        print('Please enter a single numerical value.')

def returnCalcOutput():

  # Determine value of each operation
  if operation == 'ADDITION':
    print('= ', float(value1) + float(value2))
  elif operation == 'SUBTRACTION':
    print('= ', float(value1) - float(value2))
  elif operation == 'MULTIPLICATION':
    print('= ', float(value1) * float(value2))  
  elif operation == 'DIVISION':
    print('= ', float(value1) / float(value2))
  elif operation == 'EXPONENTIATION':
    print('= ', float(value1) ** float(value2))
  elif operation == 'MODULO':
    print('= ', float(value1) % float(value2))
  elif operation == 'FLOOR DIVISION':
    print('= ', float(value1) // float(value2))
  elif operation == 'SQUARE ROOT':
    print('= ', math.sqrt(float(value1)))
  elif operation == 'X ROOT':
    print('= ', float(value2) ** (1/(float(value1))))
  elif operation == 'LOGARITHM':
    print('= ', math.log(float(value2), float(value1)))
  elif operation == 'FACTORIAL':
    print('= ', math.factorial(value1))

  # Trig ratios
  if operation == 'SINE':
    if trigUnit == 'DEGREE':
      print('= ', math.sin(float(value1)))
    else:
      print('= ', math.radians(math.sin(float(value1))))
  elif operation == 'COSINE':
    if trigUnit == 'DEGREE':
      print('= ', math.cos(float(value1)))
    else:
      print('= ', math.radians(math.cos(float(value1))))
  elif operation == 'TANGENT':
    if trigUnit == 'DEGREE':
      print('= ', math.tan(float(value1)))
    else:
      print('= ', math.radians(math.tan(float(value1))))

