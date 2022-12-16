

# Create a list of the input text
def new_input_text_list():
    input_text = open_input()
    new_list = []
    for item in input_text:
        text = item['Text']
        new_list.append(text)
    print(new_list)

#Remember to call the function from your main() otherwise it won't run.

def main():
    new_input_text_list()
    translate_loop()

#To run the program, enter the following command in the terminal:
#python lab_6_step_2_loops.py --file translate_input.json

#Using a for loop to generate new lists using .append() is a perfectly valid way of generating new lists. 
#However, we can use a list comprehension to reduce this to a single line. 
#It combines the for loop and the creation of the list into a single line.

#In lab_6_step_2_loops.py add the following below the new_input_text_list() function:

def new_list_comprehension():
    input_text = open_input()
    list_comprehension = [item['Text'] for item in input_text]
    print(list_comprehension)

#Add the function to main()

def main():
    new_input_text_list()
    translate_loop()
    new_list_comprehension()

#To run the program, enter the following command in the terminal:
#python lab_6_step_2_loops.py --file translate_input.json

