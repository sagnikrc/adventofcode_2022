file1 = open('day_01_input.txt', 'r')
Lines = file1.readlines()

max = 0
elf_cal=0
elves_cal = []
# Strips the newline character
for line in Lines:
    if line.strip() == '':
        elves_cal.append(elf_cal)
        if max < elf_cal:
            max = elf_cal
        elf_cal = 0
        #print("Line{}: {}".format(count, 'newline'))

    else:
        elf_cal += int(line.strip())

print(max)
elves_cal.sort(reverse=True)
total = 0
for i in range(0,3):
    total+= elves_cal[i]

print(total)
