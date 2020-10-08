# Lists the characters in King Lear and how many times each character speaks.

# Empty list to fill with character names.
character_list = []
# Open and read file line by line.
file = open("King_Lear.txt", "r").readlines()
# Iterate through the text, finding character names with the following logic:
#   (1) Includes all caps;
#   (2) Does not include "ACT" or ".";
#   (3) Includes all upper case letters;
#   (4) Not already in character list.
for x in file:
    if "\n" in x and "ACT" not in x and "." not in x and x.isupper() and x.strip("\n") not in character_list:
        character_list.append(x.strip("\n"))
# Pass the list of characters to a dictionary as keys, finding the number of quotes for each character as values.
character_dictionary = {character: int(file.count(character + "\n")) for character in character_list}
# Pass the character dictionary to another dictionary, sorting by value.
sorted_character_dictionary = {a: b for a, b in sorted(character_dictionary.items(),
                                                       key=lambda item: item[1], reverse=True)}
# Format and print each key and corresponding value.
for each_character in sorted_character_dictionary:
    print(each_character + ":" + str((15 - len(each_character)) * " ")
          + str(sorted_character_dictionary[each_character]))
