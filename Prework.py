#def hello_name(user_name):  
    #	print( "hello " + str(user_name.upper()) + "!")
 
#hello_name("Troy")
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#def first_odds():

    #for i in range(1, 101):
        #if i % 2 != 0:
            #print(i)
#first_odds()



 #Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


#def max_num_in_list(a_list) :  

   # if not a_list:
        #return None
    
   # max_num = a_list[0]
    #for num in a_list:
       # if num > max_num:
           # max_num = num

    #return max_num 
#numbers = [1, 25, 39, 2, 40, 28, 50]   
#print(max_num_in_list(numbers))   
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


#def is_leap_year(a_year):
   # if a_year % 4 == 0:
        #if a_year % 100 != 0 or a_year % 4 == 0:
           # return True
    #return False

#year = 2022
#print(is_leap_year(year))


#5. Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
#def is_consecutive(a_list):
   # if len(a_list) < 2:
        #return False
    #sorted_numbers = sorted(a_list)
    #for i in range(len(sorted_numbers) - 1 ):
        #if sorted_numbers[i] + 1 != sorted_numbers[i + 1]: 
            #return False
    #return True
#number1 = [1,2,3,4,5]
#number2 = [1,3,4,9]
#print(is_consecutive(number1))
#print(is_consecutive(number2))
