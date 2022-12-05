
def get_sections_from_range(input_range):
    inputs = input_range.split('-')
    return [int(input) for input in inputs]

def do_ranges_completely_overlap(first_range, second_range):
    if first_range[0] <= second_range[0] and first_range[1] >= second_range[1]:
        return True

    elif second_range[0] <= first_range[0] and second_range[1] >= first_range[1]:
        return True

    return False

def do_ranges_overlap(first_range, second_range):
    first_elf, second_elf = set(), set()
    
    for element in range(first_range[0], first_range[1]+1):
        first_elf.add(element)

    for element in range(second_range[0], second_range[1]+1):
        second_elf.add(element)
    
    return (len(first_elf.intersection(second_elf)) > 0)


file1 = open('day_4_input.txt', 'r')
Lines = file1.readlines()

completely_overlapped_counter = 0
overlapped_counter = 0

for line in Lines:
    pairs = line.split(',')

    elf_1_range = get_sections_from_range(pairs[0].strip())
    elf_2_range = get_sections_from_range(pairs[1].strip())

    #print(f'{line} {elf_1_range} {elf_2_range}')

    if do_ranges_completely_overlap(elf_1_range, elf_2_range):
        completely_overlapped_counter += 1
    if do_ranges_overlap(elf_1_range, elf_2_range):
        overlapped_counter += 1

print(completely_overlapped_counter)

print(overlapped_counter)