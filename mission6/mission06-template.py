#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:







# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(10)(0.1), 50)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: gosper_curve(50)(0), 500)

# Time measurements
#  152, 174, 171, 201, 153
#  Average = 170.2


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: gosper_curve_with_angle(50, lambda lvl: pi/4)(0), 500)

#  150, 223, 162, 201, 191
#  Average = 185.4

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

# profile_fn(lambda: your_gosper_curve_with_angle(50, lambda lvl: pi/4)(0), 500)

#  15121, 14642, 14319, 15016, 14341
#  Average = 14687.8


# Conclusion:
# Basically, function gosper_curve_with_angle and gosper_curve
# have the run time of the same time level;
# however as for function your_gosper_curve_with_angle, it tooks much more time to run.
# Specifically, the most customized function, that is, gosper_curve,took the shortest time.
# And then followed the gosper_curve_with_angle which just spends a little bit more time to run
# since it is less customized because it takes in an additional input, namely the angle.
# And the least customized, namely the most customizable function,
# your_gosper_curve_with_angle took the longest time. In short,
# customized functions are faster than those less customized (more customizable/generalized) functions.

##########
# Task 2 #
##########

#  1) Yes, joe_rotate works as the same purpose as rotate.
# joe_rotate still gets the same x and y values from the curve,and hence,returns the same thing


#  2) As for joe_rotate, pt is not initialised.Then,to get the x and y values, the function has to call x_of() and
# y_off() on curve(t) twice, so this linear step is done twice.
# As for gosper_curve, it returns repeated(gosperize, level)(unit_line) and
# gosperize calls the rotation function (rotate or joe_rotate) twice within it.
# When joe_rotate is used, the extra steps within it will be called recursively with repeated(gosperize, level)
# Hnece, the total time complexity is exponential for joe_rotate.

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <3>         <4>
#                      2         <5>         <10>
#                      3         <7>         <22>
#                      4         <9>         <46>
#                      5         <11>         <...>
#
#  Evidence of exponential growth in joe_rotate.

