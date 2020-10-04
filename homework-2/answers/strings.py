from tests import splice_tests

def splice_1():
  '''For each question, replace the "None" with your answer!'''

  flower_string = "My favorite flower is a rose!"
  goodbye_string = "Goodbye my friends."

  # q_1: splice the "Goodbye" from goodbye_string
  q_1 = goodbye_string[:7]

  # q_2: splice the "friends" from goodbye_string
  q_2 = goodbye_string[-8:-1]

  # q_3: splice the "!" from flower_string
  q_3 = flower_string[-1]

  # q_4: splice the "flower" from flower_string
  q_4 = flower_string[12:18]

  # q_5: splice the "rose!" from flower_string
  q_5 = flower_string[-5:]

  # q_6: splice the "favorite flower " from flower_string
  q_6 = flower_string[3:19]

  # q_7: splice the "." from goodbye_string
  q_7 = goodbye_string[-1]

  # q_8: splice the "My favorite flower is " from flower_string and add your favorite flower to the end
  q_8 = flower_string[:22] + "pansy."

  # q_9: splice the "My " from flower_string and concatenate it with "friend" from goodbye_string. Then, concatenate it with the " is a rose!" from flower_string
  q_9 = flower_string[:3] + goodbye_string[-8:-2] + flower_string[18:]

  return q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9

  





def main():
  results = splice_1()
  for i in range(7):
    if results[i] == splice_tests[i]:
      print("Question " + str(i + 1) + ".........ok")
    else:
      print("Question " + str(i + 1) + ".........FAIL: " + results[i])

  if (len(results[7]) > 23) and (results[7][:22] == splice_tests[7]):
    print("Question 8.........ok")
  else:
    print("Question 8.........FAIL: " + results[7])

  for i in range(8, len(results)):
    if results[i] == splice_tests[i]:
      print("Question " + str(i + 1) + ".........ok")
    else:
      print("Question " + str(i + 1) + ".........FAIL: " + results[i])
