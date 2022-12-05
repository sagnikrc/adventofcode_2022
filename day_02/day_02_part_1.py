file1 = open('day_02_input.txt', 'r')
Lines = file1.readlines()


my_score = 0
opponent_score = 0
for line in Lines:
    # if line.strip() == '':
    my_pick = line[2]
    opponent_pick = line[0]
    round_score = 0 
    if my_pick == 'X':
        round_score += 1
    elif my_pick == 'Y':
        round_score += 2
    else:
        round_score += 3
    
    # opp rock
    if opponent_pick == 'A' and my_pick == 'Y':
        round_score += 6
    elif opponent_pick == 'A' and my_pick == 'X':
        round_score += 3
    
     # opp paper
    elif opponent_pick == 'B' and my_pick == 'Z':
        round_score += 6
    elif opponent_pick == 'B' and my_pick == 'Y':
        round_score += 3

     # opp scissor
    elif opponent_pick == 'C' and my_pick == 'X':
        round_score += 6
    elif opponent_pick == 'C' and my_pick == 'Z':
        round_score += 3

    else:
        round_score += 0

    my_score += round_score

    print(f'opponent = {line[0]} | me = {line[2]} | myround_score = {round_score}' )


print(f'final score = {my_score}')