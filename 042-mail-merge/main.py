with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    for name in names:
        name_wo_strip = name.strip("\n")
        with open("./Input/Letters/starting_letter.txt") as starting_letter:
            letter = starting_letter.read()
            ready_to_send = letter.replace("[name]", name_wo_strip)
            with open(f"./Output/letter_for_{name_wo_strip}.txt", "w") as final_letter:
                final_letter.write(ready_to_send)
