#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
namelist=['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(namelist)
name1=input("Choose a person from the list to replace:")
name2=input("Enter the replacement:")
index=namelist.index(name1)
namelist[index]=name2
print(namelist)
