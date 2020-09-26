## IMPORTANT: DO NOT EDIT THIS FILE ##

import part1
import part2
import part3

not_done = True
while not_done:
  trying = input("Which file would you like to run?\n")
  not_done = False
  if trying == "part1":
    part1.main()
  elif trying == "part2":
    part2.main()
  elif trying == "part3":
    part3.main()
  else:
    not_done = True
    print("Invalid file, please try again.")