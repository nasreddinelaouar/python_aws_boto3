
#how to provide user input when the program is run and pass this to the function Step_1_console_input.py

import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()
    
    
#To pass input to our function when we run Step_1_console_input.py we need to use a built-in function called input(). 
#This will prompt the user with a message and then wait for them to provide input.

#Modify your program to accept user input:
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

text = input("Provide the text you want translating: ")
source_language_code = input("Provide the two letter source language code: ")
target_language_code = input("Provide the two letter target language code: ") 

def main():
    translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )

if __name__=="__main__":
    main()
    
#To run the program, enter the following command in the terminal:

#python step_1_console_input.py

#When you run your program you should get the following prompts:

#Provide the text you want translating: 
#Provide the two letter source language code:
#Provide the two letter target language code: 
