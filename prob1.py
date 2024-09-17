def optimize_array(sequence):
    for position in range(1, len(sequence)):
        current_element = sequence[position]
        previous_index = position - 1
        while previous_index >= 0 and sequence[previous_index] > current_element:
            sequence[previous_index + 1] = sequence[previous_index]
            previous_index -= 1
        sequence[previous_index + 1] = current_element
    return sequence

array_count = int(input("Enter the number of arrays: "))
elements_per_array = int(input("Enter the number of elements per array: "))

input_arrays = []
combined_sequence = []

for _ in range(array_count):
    new_array = list(map(int, input("Enter a sorted array: ").split()))
    input_arrays.append(new_array)

for sub_array in input_arrays:
    combined_sequence.extend(sub_array)

print("Merged and sorted result:", optimize_array(combined_sequence))

'''
Example output:
Enter the number of arrays: 3
Enter the number of elements per array: 4
Enter a sorted array: 1 3 5 7
Enter a sorted array: 2 4 6 8
Enter a sorted array: 0 9 10 11
Merged and sorted result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Enter the number of arrays: 3
Enter the number of elements per array: 5
Enter a sorted array: 1 3 5 7 8
Enter a sorted array: 2 4 6 9 10
Enter a sorted array: 0 11 13 14 15
Merged and sorted result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
'''