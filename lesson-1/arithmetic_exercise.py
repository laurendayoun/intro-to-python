"""
Use what you have learned to answer the following questions.
"""

from ignore import arithmetic_tests

def question_1():
  '''
  What is the answer to 3 plus 5 plus 27 minus 73 plus 46?
  '''
  ans = 0 # replace this with your arithmetic code!
  return ans

def question_2():
  '''
  What is the answer to -12 multiplied by 5 then added to 27?
  '''
  ans = 0 # replace this with your arithmetic code!
  return ans

def question_3():
  '''
  What is the answer to (5 plus 24) multiplied by (15 minus 4) multiplied by 9 then divided by 3?
  '''
  ans = 0 # replace this with your arithmetic code!
  return ans


def question_4():
  '''
  What is the remainder when 176592 is divided by 28?
  '''
  ans = 0 # replace this with your arithmetic code!
  return ans


def question_5():
  '''
  What is the remainder when (6 + 36)^5 - 18492 is divided by 296?
  '''
  ans = 0 # replace this with your arithmetic code!
  return ans

def question_6():
  ''' (24 + 9)^5 - (871398/11)
  What is the answer to (24 + 9) to the fifth power subtracted by (871398 divided by 11) all divided by 5 squared?
  '''
  ans = 0 # replace this with your arithmetic code!
  return ans



def pretty_print(result, expected):
  status = "----Correct----" if expected == result else "----Incorrect----" 
  print(status)
  print("The answer should be: " + str(expected))
  print("Your answer is: " + str(result))
  return status[4] == "C"

def main():
  qs = [question_1(), question_2(), question_3(), question_4(), question_5(), question_6()]

  cor = 0

  for i in range(len(qs)):
    print("Question " + str(i+1))
    a = pretty_print(qs[i], arithmetic_tests[i])
    if a:
      cor += 1
  
  print("Got " + str(cor) + "/" + str(len(qs)) + " correct")