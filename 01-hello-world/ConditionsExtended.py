Name = "John"
Age = 19
Height = 10.0
Fruit = "Apple"

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
# EXTENDED CONDITIONS (if / elif / else)
#
# elif means "else if". It adds extra branches to a decision.
#   - One if at the start (required)
#   - As many elif as needed (optional)
#   - One else at the end (optional, the fallback)
#
# Python checks each condition from TOP to BOTTOM.
# It runs ONLY the first branch that is True, then skips the rest.
#
# In this program (1 decision, 5 branches):
#   Branch 1: if Age < 16               -> prints Age
#   Branch 2: elif Age == 19            -> prints Height
#   Branch 3: elif Height + Age > 30.0  -> prints Name
#   Branch 4: elif Age + Height <= 29.0 -> prints Fruit
#   Branch 5: else                      -> prints Name
#
# Result with Age = 19 and Height = 10.0:
#   1. Age < 16   -> 19 < 16   -> False, skip
#   2. Age == 19  -> 19 == 19  -> True, run print(Height)
#   Output: 10.0
#   Branches 3, 4 and 5 are never checked, because branch 2 was True first.

if Age < 16:
    print(Age)

elif Age == 19:
    print(Height)

elif Height + Age > 30.0:
    print(Name)

elif Age + Height <= 29.0:
    print(Fruit)

else:
    print(Name)

