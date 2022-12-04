file1 = open('day_3_input.txt', 'r')
Lines = file1.readlines()
priority_sums = 0
for line in Lines:
    first_compartment = line[0:len(line)//2]
    second_compartment = line[len(line)//2:len(line)]


    common = set(first_compartment).intersection(set(second_compartment))

    #print(ord('b') - 96)
    #print(ord('B') - 38)
    for element in common:
        if element.isupper():
            #print(f'{element}: upper')
            priority_sums += ord(element) - 38
        else:
            #print(f'{element}: lower')
            priority_sums += ord(element) - 96


    #print(f'{line} | first: {first_compartment} | second: {second_compartment} | common: {common}' )

print(priority_sums)