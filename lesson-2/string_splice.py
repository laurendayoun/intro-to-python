from tests import splice_tests

def splice_1():
  '''For each question, replace the "None" with your answer!'''

  hello_string = "Hello World!"
  name_string = "My name is Fernando."

  # q_1: splice the "Hello" from hello_string
  q_1 = "None"

  # q_2: splice the "World" from hello_string
  q_2 = "None"

  # q_3: splice the "!" from hello_string
  q_3 = "None"

  # q_4: splice the "name" from name_string
  q_4 = "None"

  # q_5: splice the "Fernando." from name_string
  q_5 = "None"

  # q_6: splice the "My name is " from name_string
  q_6 = "None"

  # q_7: splice the "." from name_string
  q_7 = "None"

  # q_8: splice the "My name is " from name_string and add your name to the end
  q_8 = "None"

  # q_9: splice the "World" from hello_string and concatenate it with " is " from name_string. Then, add "beautiful!" at the end.
  q_9 = "None"

  # q_10: splice the "Hello " from hello_string and concatenate it with "Fernando" from name_string. Then, concatenate it with the "!" from hello_string
  q_10 = "None"

  return q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10

  





def main():
  results = splice_1()
  for i in range(7):
    if results[i] == splice_tests[i]:
      print("Question " + str(i + 1) + ".........ok")
    else:
      print("Question " + str(i + 1) + ".........FAIL: " + results[i])

  if (len(results[7]) > 12) and (results[7][:11] == "My name is "):
    print("Question 8.........ok")
  else:
    print("Question 8.........FAIL: " + results[7])

  for i in range(8, len(results)):
    if results[i] == splice_tests[i]:
      print("Question " + str(i + 1) + ".........ok")
    else:
      print("Question " + str(i + 1) + ".........FAIL: " + results[i])
