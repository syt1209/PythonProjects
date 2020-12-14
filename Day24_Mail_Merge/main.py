PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_body = letter_file.read()
    for name in names:
        new_letter = letter_body.replace(PLACEHOLDER, name.strip())
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.docx", mode="w") as complete_letter:
            complete_letter.write(new_letter)
