'''
Find if 6 is available in the list [4, 8, 7, 4, 3, 6, 2, 1, 9].
'''

numbers = [4, 8, 7, 4, 3, 6, 2, 1, 9]

if 6 in numbers:
    index_of_6 = numbers.index(6)
    print(f"6 is available in the list at index {index_of_6}.")
else:
    print("6 is not available in the list.")
