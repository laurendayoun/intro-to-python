from tests import list_tests

def lists_1():
  '''For each question, replace the "None" with your answer!
  From question 3 onwards, you are not allowed to hardcode the answer.
  '''

  # q_1: create a list with the elements 1, 2, and 3 (in that order)
  q_1 = "None"

  # q_2: create a list with the 4 fruits, where the starting letter of each fruit is a, b, c, and d (in that order)
  q_2 = "None"

  # q_3: create a list with the elements 10, 14, and 27 (in that order) repeated 7 times
  q_3 = "None"

  # q_4: create a list with the elements 8, 12, and 16 (in that order) repeated 6 times, and then with another 8 and 12
  q_4 = "None"

  odds_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

  # q_5: splice values 3-13 from odds_list
  q_5 = "None"

  # q_6: index the value 11 from odds_list
  q_6 = "None"

  # q_7: splice values 11-19 from odds_list and add 21 to the end
  q_7 = "None"

  # q_8: get values 15 and 19 from odds_list (as a list, so your result should be [15, 19])
  # Hint: there are multiple ways to do this question!
  q_8 = "None"

  # q_9: remove 9 from odds_list
  # For this question, you should change odds_list in a separate code statement. Do not edit the q_9 variable!

  ### YOUR CODE HERE ###


  ######################
  q_9 = odds_list[:]

  # q_10: add 21 and 23 to odds_list, in that order
  # For this question, you should change odds_list in a separate code statement. Do not edit the q_10 variable!

  ### YOUR CODE HERE ###


  ######################
  q_10 = odds_list[:]

  return q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10


def main():
  results = lists_1()
  if results[0] == list_tests[0]:
    print("Question 1.........ok")
  else:
    print("Question 1.........FAIL: " + str(results[0]))

  correct = True
  for f in range(4):
    if results[1][f][0] != list_tests[1][f]:
      print("Question 2.........FAIL: " + str(results[1]))
      correct = False
      break
  if correct:
    print("Question 2.........ok")
  
  for i in range(2, len(results)):
    if results[i] == list_tests[i]:
      print("Question " + str(i + 1) + ".........ok")
    else:
      print("Question " + str(i + 1) + ".........FAIL: " + str(results[i]))

