#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        fixed_name = name.strip()
        with open("./Input/Letters/starting_letter.txt") as letter_file:
            letter = letter_file.read()
            done_letter = letter.replace("[name]", f"{fixed_name}")
            with open(f"./Output/ReadyToSend/{fixed_name}.invitation.txt", mode="w") as invite:
                invite.write(done_letter)



