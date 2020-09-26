"""
Use what you have learned to answer the following questions.

Answer options are:
string, int, float, bool, error
"""

from ignore import type_tests

def question_1():
  ''' 
  What is the type of 'Hello World'?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_2():
  '''
  What is the type of 'Hello World ' + 'fellow coder'?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_3():
  '''
  What is the type of 42?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_4():
  '''
  What is the type of '42'?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_5():
  '''
  What is the type of '127 + 31'?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_6():
  '''
  What is the type of 46.98?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_7():
  '''
  What is the type of '84.3'?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_8():
  '''
  What is the type of 6/3?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_9():
  '''
  What is the type of 6/3.0?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_10():
  '''
  What is the type of 176592/28?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_11():
  '''
  What is the type of the remainder when 176592 is divided by 28?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_12():
  '''
  What is the type of the quotient when 176592 is divided by 28?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_13():
  '''
  What is the type of 13 = 13?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_14():
  '''
  What is the type of 13 == 13?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_15():
  '''
  What is the type of 13 + 27 == 27 + 13?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_16():
  '''
  What is the type of 13 + 27 == '27' + '13'?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_17():
  '''
  What is the type of 70 < 149?
  '''
  ans = "" # replace this with your answer!
  return ans

def question_18():
  '''
  What is the type of '38 > 19'?
  '''
  ans = "" # replace this with your answer!
  return ans



def main():
  qs = [question_1(), question_2(), question_3(), question_4(), question_5(), question_6(), question_7(), question_8(), question_9(), question_10(), question_11(), question_12(), question_13(), question_14(), question_15(), question_16(), question_17(), question_18()]

  for i in range(len(qs)):
    cor = 0
    if qs[i] == type_tests[i]:
      cor += 1
      print("Question " + str(i+1) + ".........ok")
    else:
      print("Question " + str(i+1) + ".........FAIL")
    
  print("Got " + str(cor) + "/" + str(len(qs)) + " correct")
