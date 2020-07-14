#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
########################################################

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    """ Write your code here """
    this_table=get_table_state(table)
   
    flip_coins(table,this_table)
    
        
    

# test:
#t2_1 = create_table(2)
#solve_trivial_2(t2_1)
# print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_1_run = create_table(2)
# run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_1_susan = create_table(2)
# Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    """ Write your code here """
    this_table=get_table_state(table)
   
    flip_coins(table,this_table)
    
        

# test:
# t4_2 = create_table(4)
# solve_trivial_4(t4_2)
# print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_2_run = create_table(4)
# run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_2_susan = create_table(4)
# Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    """ Write your code here """
    if check_solved(table)==False:
        flip_coins(table,(1,0))

# test:
# t2_3 = create_table(2)
# solve_2(t2_3)
# print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t2_3_run = create_table(2)
# run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    """ Write your code here """
    
    proce=((1,1,1,1),(1,0,1,0),(1,1,0,0),(1,0,0,0))
    count=0
    while check_solved(table)==False:
        count=count+1
        for i in range(2,-1,-1):
            if count%(2**i)==0:
                flip_coins(table,proce[i+1])
                print(i)
                break
            
            
        

# test:
#t4_4 = create_table(4)
#solve_4(t4_4)
#print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

# t4_4_run = create_table(4)
# run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    """ Write your code here """
    def pro(size):

        if size==1:
            return ((1,1),(1,0))
    
        zero=(0,0)
        this_table=()
        original_t=((1,1),(1,0))
        this_size=2
        for i in range(size-1):
            for j in range(this_size):              
                this_table=this_table+(original_t[j]+original_t[j],)
            for j in range(this_size):
                this_table=this_table+(original_t[j]+zero,)

            zero=zero+zero
            original_t=this_table
            this_table=()
            this_size=this_size*2

        return original_t
    
    size= get_table_size(table)
    

    lgsize=round(log2(size))
    proce=pro(lgsize)

    count=0

    while check_solved(table)==False:
        count=count+1
        for i in range(size-1,-1,-1):
            if count%(2**i)==0:
             
                flip_coins(table,proce[i+1])
                break
    
    
            
    
            



# test:
t4_5 = create_table(4)
solve(t4_5)
print(check_solved(t4_5))

t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
