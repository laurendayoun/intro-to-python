import string_splice
import lists
import forloops

to_run = input("Which file do you want to run?\n")
if to_run == "lists":
  lists.main()
elif to_run == "string_splice":
  string_splice.main()
elif to_run == "forloops":
  forloops.main()