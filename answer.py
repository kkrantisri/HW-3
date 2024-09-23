
import math

def calculate():
    a=3
    b=4

    # Add a and b then assign the sum to variable c

    # Subtract c by 1 then divide this result by 5.0 and assign this final result to the variable q

    # Assign the type of the variable q to a new variable type_q

    return c,q,type_q


def string_formating():

    math_pi = 3.141592653589793

    # Format the variable math_pi as a string with 6 decimal places and assign it to variable string_pi

    ####
    large_number=100000000

    # Format large_number to be a string and assign it to the variable comma_string. The contents of comma_string
    # should have the appropriate commas. (Comma separator). Example; 1000 should be "1,000"

    # Format large_number to be a string and assign it to the variable exp_string. The contents of exp_string
    # should be exponent notation (with two decimal places).

    ####
    small_number =13

    # Format small_number to be a string and assign it to the variable center_string. 
    # The format for center_string should be Center aligned with a width of 10.

    # Format small_number to be a string and assign it to the variable left_string.
    # The format for left_string should be Left aligned with a width of 10.

    return string_pi,comma_string,exp_string,center_string,left_string


def build_in():
    #### Use the math library for the following questions.
    # Assign the number pi to the variable math_pi

    # Assign the Euler's number (e) to the variable math_e

    # Assign the sine of pi (sin(pi)) to the variable sin_pi

    # Assign the square root of 2 to the variable square_root_2

    # Assign the absolute value of -2 to the variable abs_2
    # (Please use the built-in Python function for absolute value)

    return math_pi,math_e,sin_pi,square_root_2,abs_2



def set_op():
    S1 = {1, 2, 3, 4}
    S2 = {3, 4, 5, 6}

    # Add 0 to set S1

    # Assign the union of S1 and S2 to the variable union_s

    # Assign the sum of all items in union_s to the variable sum_s

    return S1,union_s,sum_s


calculate()
string_formating()
build_in()
set_op()
