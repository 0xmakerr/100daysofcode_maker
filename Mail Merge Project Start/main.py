#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()
name_list = [name.strip() for name in name_list]

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter = letter.read()

replace = "[name]"
for name in name_list:
    letter = letter.replace(f"{replace}", f"{name}")
    with open(f"./Output/ReadyToSend/{name}", mode="w") as finished_letter:
        finished_letter.write(letter)
    replace = name
    