# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
file1 = open("./Input/Letters/starting_letter.txt", "r")
file2 = open("./Input/Names/invited_names.txt", "r")
names = file2.readlines()
letter = file1.read()

for name in names:
    new_letter = letter.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/{name.strip()}.txt", "w+") as f:
        f.write(new_letter)


# print(letter)
file1.close()
file2.close()

