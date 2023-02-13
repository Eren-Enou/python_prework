#Question 1
#Function that prints "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name="USERNAME"):
    print("hello_"+str(user_name).upper()+"!")

#Question 2
#Function that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    #iterate from 1 - 100
    for i in range(1, 101):
        #Check if remainder from dividing by 2
        if i % 2 == 1:
            print(i)
                
#Question 3
#Function that returns the max number of a given list.
def max_num_in_list(a_list):
    #Check if list is empty
    if not a_list:
        return None
    #Initialize max_num with first element of list
    max_num = a_list[0]
    #iterate over list
    for num in a_list:
        #if element is greater than max, update max
        if num > max_num:
            max_num = num
    return max_num
    
#Question 4
#Function that returns if the given year is a leap year.
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                #divisible by 4, 100, and 400
                return True
            #divisible by 4 and 100, not 400
            else:
                return False
        #divisible by 4 and not 100
        else:  
            return True
    #not divisible by 4        
    else:
        return False

#Question 5
#Function to check to see if all numbers in list are consecutive numbers.
def is_consecutive(a_list):
    # Check if list is empty
    if not a_list:
        return True
    # Check if list has only one element
    if len(a_list) == 1:
        return True
    # Check if numbers in list are consecutive
    for i in range(1, len(a_list)):
        if a_list[i] - a_list[i-1] != 1:
            return False
    # If checks pass, return True
    return True
