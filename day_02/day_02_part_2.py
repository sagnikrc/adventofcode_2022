file1 = open('day_02_input.txt', 'r')
Lines = file1.readlines()

my_score = 0
opponent_score = 0
for line in Lines:
    # if line.strip() == '':
    outcome = line[2]
    opponent_pick = line[0]
    round_score = 0 

    # X means you need to lose, 
    # Y means you need to end the round in a draw
    # and Z means you need to win

    if outcome == 'X':
        round_score += 0
    elif outcome == 'Y':
        round_score += 3
    else:
        round_score += 6

    # opp rock
    if opponent_pick == 'A' and outcome == 'X': # choose scissor
        round_score += 3
    if opponent_pick == 'A' and outcome == 'Y': # choose rock
        round_score += 1
    if opponent_pick == 'A' and outcome == 'Z': # choose paper
        round_score += 2
    
     # opp paper
    if opponent_pick == 'B' and outcome == 'X': # choose rock
        round_score += 1
    if opponent_pick == 'B' and outcome == 'Y': # choose paper
        round_score += 2
    if opponent_pick == 'B' and outcome == 'Z': # choose scissor
        round_score += 3

     # opp scissor
    if opponent_pick == 'C' and outcome == 'X': # choose paper
        round_score += 2
    if opponent_pick == 'C' and outcome == 'Y': # choose scissor
        round_score += 3
    if opponent_pick == 'C' and outcome == 'Z': # choose rock
        round_score += 1

    my_score += round_score

    print(f'opponent = {line[0]} | outcome = {line[2]} | myround_score = {round_score}' )


print(f'final score = {my_score}')