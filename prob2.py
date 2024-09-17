def eliminate_duplicates(sequence):
    if not sequence:
        return []
    
    
    length = len(sequence)
    unique_index = 0
    
    for current_index in range(1, length):
        if sequence[current_index] != sequence[unique_index]:
            unique_index += 1
            sequence[unique_index] = sequence[current_index]
    
    return sequence[:unique_index + 1]

raw_input = input("Please enter a sorted sequence of numbers: ")
original_sequence = list(map(int, raw_input.split()))
cleaned_sequence = eliminate_duplicates(original_sequence)

print(f"Initial sequence: {original_sequence}")
print(f"Sequence after duplicate removal: {cleaned_sequence}")

'''
Example
Please enter a sorted sequence of numbers: 3 3 3 3
Initial sequence: [3, 3, 3, 3]
Sequence after duplicate removal: [3]

Please enter a sorted sequence of numbers: 1 2 2 3 4 4 4 5 5
Initial sequence: [1, 2, 3, 4, 5, 4, 4, 5, 5]
Sequence after duplicate removal: [1, 2, 3, 4, 5]
'''