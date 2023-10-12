#!/usr/bin/env python3

# 2. Write a script that splits a string into a list. In your script:

#Save the string sapiens, erectus, neanderthalensis as a variable named taxa.
taxa = 'sapiens, erectus, neanderthalensis'

#Print taxa.
print(taxa)

#Print taxa[1], what do you get?
print(taxa[1])
## O resultado obtido é a letra a, o segundo caractere da string.

#Print type(taxa). What is it's type?
print(type(taxa))
## O tipo é string.

#Split taxa into individual words and print the result of the split. (Think about the ', '.)
taxa.split(', ')

#Store the result of split in a new variable named species.
species = taxa.split(', ')

#Print species.
print(species)

#Print the species[1], What do you get?
print(species[1])
## É imprimida a palavra "erectus", que é o primeiro elemento da lista.

#Print type(species). What is it's type?
print(type(species))
## O tipo é lista.

#Sort the list alphabetically and print (hint: lookup the function sorted()).
sorted_species = sorted(species)
print(sorted_species)

#Sort the list by length of each string and print. (The shortest string should be first). Check out documentation of the key argument.
sorted_by_length_species = sorted(species, key = len)
print(sorted_by_length_species)
