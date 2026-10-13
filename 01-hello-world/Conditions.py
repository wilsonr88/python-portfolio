Name = "John"
Age = 19
Height = 10.0
# CONDITIONS (if / else)
#
# A condition is a question that is either True or False.
# Python uses it to decide which code to run.
#
#   if <condition>:     -> runs the indented code below ONLY if the condition is True
#   else:               -> runs the indented code below if the condition is False
#
# Comparison operators you can use in a condition:
#   <    less than
#   >    greater than
#   <=   less than or equal to
#   >=   greater than or equal to
#   ==   equal to (two equals signs; one = is for setting a variable)
#   !=   not equal to
#
# Rules to remember:
#   - Put a colon (:) at the end of the if and else lines.
#   - Indent the code that belongs to each part (VS Code uses 4 spaces).
#   - else has no condition; it catches everything the if didn't.
#
# In this program:
#   if Age < 16  -> True when Age is 15 or less, so it prints Age
#   else         -> covers Age 16 or more, so it prints Name
#   With Age = 19, the condition is False, so it prints "John".

if Age < 16:
    print(Age)

else:
    print(Name)
