print("Program starting.")
compound = input("\nInsert a closed compound word: ")
length = len(compound)
first = compound[0]
lastnum = len(compound) - 1
last = compound[lastnum]
reverse = compound[::-1]
print(f"The word you inserted is '{compound}' and in reverse it is '{reverse}'.")
print(f"The inserted word length is {length}")
print(f"Last character is '{last}'")
print("\nTake substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
end = min(end, len(compound))
sub = compound[start:end:step]
print(f"\nThe word '{compound}' sliced to the defined substring is '{sub}'.")
print("Program ending.")
