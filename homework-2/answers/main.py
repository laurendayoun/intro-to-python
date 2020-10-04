import strings
import lists
import forloops

to_run = input("Which file do you want to run?\nOptions are: strings, lists, forloops\n")
if to_run == "lists":
  lists.main()
elif to_run == "strings":
  strings.main()
elif to_run == "forloops":
  forloops.main()