from tests import list_tests

def lists_1():
  '''For each question, replace the "None" with your answer!
  From question 3 onwards, you are not allowed to hardcode the answer.
  '''

  # q_1: create a list with the elements 5, 10, and 15 (in that order)
  q_1 = [5, 10, 15]

  # q_2: create a list with 5 veggies, where the starting letter of each fruit is a, b, c, d, and e (in that order)
  q_2 = ['asparagus', 'bean sprout', 'carrot', 'dill', 'eggplant']

  # q_3: create a list with the elements 4, 8, 12, and 16 (in that order) repeated 5 times
  q_3 = [4, 8, 12, 16] * 5

  # q_4: create a list with the elements 3, 6, and 9 (in that order) repeated 6 times, and then with 10 and 11 added at the end
  q_4 = [3, 6, 9] * 6 + [10, 11]

  nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

  # q_5: splice all numbers between 4 - 25 from nums
  q_5 = nums[3:7]

  # q_6: index the number 13 from nums
  q_6 = nums[5]

  # q_7: splice values 10-50 from nums and add [53, 59] to the end
  q_7 = nums[5:8] + [53, 59]

  # q_8: get values 13, 34, and 89 from nums (as a list, so your result should be [13, 34, 89])
  # Hint: there are multiple ways to do this question!
  q_8 = [nums[5], nums[7], nums[9]]



  # q_9: remove 8 from nums
  # For this question, you should change nums in a line of code. Do not edit the q_9 variable!
  ### YOUR CODE HERE ###
  nums.pop(4)


  ######################
  q_9 = nums[:]



  # Challenge q_10 (optional): Add up the last two elements in nums and add it to the end of nums. Do this 2 times (the final list should have 12 numbers in it)
  # Do not edit the q_10 variable!

  ### YOUR CODE HERE ###
  nums.append(nums[-1] + nums[-2])
  nums.append(nums[-1] + nums[-2])

  ######################
  q_10 = nums[:]

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
