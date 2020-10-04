"""
Reminders:
for loop format:
  for ELEMENT in GROUP:
    BODY
  - ELEMENT can be any variable name, as long as it doesn't conflict with other variables in the loop
  - GROUP will be a list, string, or range()
  - BODY is the work you want to do at every loop
  
range format is:
  range(start, stop, step) or range(start, stop) or range(stop)
  - if step not given, step = 1; if start not given, start = 0
  - if step is negative, we decrease
"""

def forloop_1():
  '''Create a for loop that prints every element in the list numbers'''
  numbers = [5, 10, 15, 20, 25, 30]
  ### Your code here ###




def forloop_1_2():
  '''Create a for loop that prints every multiple of 5 from 5 to 30'''
  # Hint: Use range. You are not allowed to use a list!
  ### Your code here ###




def forloop_2():
  '''Create a for loop that adds together all of the strings in words. 
  
  Your final string should be: My name is <name>. Replace <name> with your name in the list!'''
  words = ["My ", "name ", "is ", "<name>"]
  sentence = ""
  ### Your code here ###






  print("The string is: " +  sentence)



def forloop_2_2():
  '''Create a for loop that adds together all of the strings in words. Every time you add a word, add a space (" ") so that the sentence is easy to read! 
  
  Your final string should be: My name is <name>. Replace <name> with your name in the list!'''
  words = ["My", "name", "is", "<name>"]
  sentence = ""
  ### Your code here ###





  print("The string is: " +  sentence)



def forloop_3():
  '''Create a for loop that doubles (multiplies by 2) the variable a 7 times.
  
  The final value of a should be 128.'''
  a = 1
  ### Your code here ###





  print("Your result is: " + str(a))



def forloop_4():
  '''Create a for loop that prints the numbers, and then the letters in mixed_list
  
  The order of things printed should be: 1, 3, 5, b, d, f'''
  mixed_list = [1, 'b', 3, 'd', 5, 'f']
  ### Your code here ###






def forloop_5():
  '''Challenge Question (optional):
  Code 2 different programs that print:
  5
  4
  3
  2
  1
  Take off!
  Hint: Use a list in one program, and range in another. '''
  ### Your code here ###



def main():
  print("Question 1:")
  forloop_1()
  print("\nQuestion 1.2:")
  forloop_1_2()
  print("\nQuestion 2:")
  forloop_2()
  print("\nQuestion 2.2:")
  forloop_2_2()
  print("\nQuestion 3:")
  forloop_3()
  print("\nQuestion 4:")
  forloop_4()
  print("\nQuestion 5:")
  forloop_5()