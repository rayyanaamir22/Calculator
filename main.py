'''
Name: Rayyan Aamir
Date: December 22, 2021
Program: Improved Single Operation Calculator
'''

'''
Issue: DEGREES does not register as default unit until it is explicitly chosen from MODE
'''

# Modules
import calcFunctions
import os

# Main Functions
def useAgain():
  print('\nDo you want to use the calculator again? (yes or no)')
  while True:
    useAgain = input()
    if useAgain.startswith('y'):
      os.system('clear')
      return True
    elif useAgain.startswith('n'):
      os.system('clear')
      return False
    else:
      print('Invalid input')

# Program loop

while True:
  print(f'C A L C U L A T O R    ({cf.currentUnit})')

  cf.getCalcOperation()
  cf.setOperationSymbol()
  cf.getCalcInput()
  cf.returnCalcOutput()
  if useAgain():
    continue
  else:
    break
