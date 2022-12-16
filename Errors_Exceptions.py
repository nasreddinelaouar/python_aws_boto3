#Modify your code to add the try-except.

import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(err))

#This should return:

#WARNING\:root\:Error - must be str, not int. You cannot add a string to an integer, without converting the integer to a string first
