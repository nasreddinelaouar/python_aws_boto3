#import json

# This uses a json string as an input
#json_string = """
#{
#    "Input":[
#        {
#        "Text":"I am learning to code in AWS",
#       "SourceLanguageCode":"en",
#        "TargetLanguageCode":"fr"
#        }
#    ]
#}
#"""

#json_input = json.loads(json_string)

# Defines two variables to store the language code from the input.
#SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
#TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
#if SourceLanguageCode == TargetLanguageCode:
#    print("The SourceLanguageCode is the same as the TargetLanguageCode - stopping")
#else:
#   print("The Source Language and Target Language codes are different - proceeding")



#We have used print() to output the messages to the console. This is where we need to make changes to the code to add them to logs rather than output to the console.#
#First, we need to import logging and then amend the print() statements with the relevant level for the message.
#Amend the code as shown below to remove print() and replace it with logging.warning and logging.info .



# Import logging
import logging
import json

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - stopping") # This will print to the console as the default level is warning
else:
    logging.info("The Source Language and Target Language codes are different - proceeding") # This will not print to the console because it is lower than warning
    
    
    