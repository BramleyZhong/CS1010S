#
# CS1010S --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <A0194525Y> <Gao Haochun>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x,x)

# (a) What are the types of the input and output of the generic square operation?(1 mark)
# Answer: (Generic-Num, Generic-Num) -> Generic-Num

# (b) Why would we prefer to define square in the above way, rather than: (2 marks)
# def square(x):
#    return apply_generic("square",x)

# Answer: Because using apply_generic("square", x) need to add
# an additional row/operation in the _operation_table, and an operation for each number package.
# If we use "mul", then it can work for the different number packages.



##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by
# the name of the operator and a tuple of strings. For example, the add operator is indexed
# by ’add ord’ and (’ordinary’, ’ordinary’); negation is indexed by ’negate ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by ’make ord’ and just a string ’ordinary’.
# Explain why we have such a difference.
# Hint: Consider the differences in the process of the creation of a Generic-Num, such as create ordinary,
# and the operations we can apply on Generic-Num, such as add. How is make ord invoked, and how is add ord invoked?

# Answer: The generic number operators like "add", "negation" used "apply_generic",
# whose intemediate step is to get a tuple mapping the "type_tag" of each argument.
# This is passed to the "get" operator, then we look up the table with the tuple of tags.
# While "make_ord" in the _operations_table is only called by "create_ordinary(x)", which only has a
#string "ordinary", hence it is indexed by the string "ordinary"


##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

# first_try = create_rational(9, 10)
# second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way:second_try
# What happens: raise Exception('Bad tagged datum -- type_tag ', 9)
# Why it happens: If we do like the first_try, the rational numbers are then repreented as tuples of ('rational', (9, 10))
# instead of ('rational', (('ordinary', 9), ('ordinary', 10))).
# When we use ('rational', (9, 10)) as input of the apply_generic function, the "proc(*map(content, args))" will
# call "add_rat((9, 10), (3, 10))", which calls the generic operator "mul" to the numerator/denominators,
# and this should be tagged of data type instead of numbers(python-integer).

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 =create_rational(create_ordinary(2), create_ordinary(7 
# r3_1 =create_rational(create_ordinary(3), create_ordinary(1))
# csq = square(sub(r2_7, r3_1))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |       |       |  -->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |       |       |
##            +---+---+---+---+
##                |       |
##                v       v

  

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x,y))
    def reprat(x,y):
        return (x,y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add,sub,mul,div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x,y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x,y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x,y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x,y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )
    def negate_rat(x):
        # input is a rational number and output is also a rational number
        return make_rat(negate(numer(x)), denom(x))
    
    def is_zero_rat(x):
        # input is a rational number and output is a boolean
        return is_zero(numer(x))
    
    def is_eq_rat(x,y):
        # inputs are two rational numbers and output is a boolean
        return is_zero(sub_rat(x,y))
    put("make","rational", make_rat)
    put("add",("rational","rational"), add_rat)
    put("sub",("rational","rational"), sub_rat)
    put("mul",("rational","rational"), mul_rat)
    put("div",("rational","rational"), div_rat)
    put("negate", ("rational",), negate_rat)
	put("is_zero", ("rational",), is_zero_rat)
	put("is_equal", ("rational", "rational")


install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

######################################################
# Change the value for variable: r1_2, r2_4 and r1_8 #
######################################################
r1_2 = None
r2_4 = None
r1_8 = None

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
