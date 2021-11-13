#Variables used in the code
user_input = ""
output_list = []
final_output = ""
find = False
questions = ["who", "what", "where", "when", "why", "how"]

#Keeps loop running until "\end" is entered
while True:
    #user input and find flag reset
    user_input = input("Say something: ")
    find = False
    
    #break out of loop
    if user_input == "\end":
        break

    #checks to see if input has a word from the questions list located in the variables. If word is found then a "?" is added to the end of the sentence 
    for question in questions:
        if user_input.find(question) != -1:
            output_list.append(user_input+"?")
            find = True
            break
    
    #check to see if questions was found and if not the add a "." to the end of the sentence
    if find == False:
        output_list.append(user_input+".")
        
#Adds all the statments into a single string and prints the output
print(" ".join(output_list))

#NOTES:
#1. Could have accounted for capitalization
#2. could account for empty inputs
#3.