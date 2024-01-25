with open("input/Letters/starting_letter.txt") as letter:
  letter_content = letter.read()
  print(letter_content)

with open("input/Names/invited_names.txt") as invited_names:
  invited_names_content = invited_names.readlines()
  print(invited_names_content)

for name in invited_names_content:
  name_clear = name.strip("\n")
  with open(f"output/ReadytoSend/{name_clear}_invite.txt", "w") as new_invite:
    new_invite.write(letter_content.replace("[name]", name_clear))


