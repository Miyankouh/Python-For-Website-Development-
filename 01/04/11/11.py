from data11 import teams
""" قسمت 11 و 12"""



print('--------------------')

lambda team: team['score'] * 9

print('--------------------')







def parse_result(team):
    # win_msg =  f" win: {team['result'].count('w')}".ljust(10)
    # lose_msg = f"lose: {team['result'].count('l')}".ljust(10)
    # draw_msg = f"draw: {team['result'].count('d')}".ljust(10)
    # team_name = f"name: {team['name']}".ljust(20)

    # print(team_name + win_msg + lose_msg + draw_msg)

#Todo: optimize finding count of win , lose and draw
    return {
        'name': team['name'],
        'win': team['result'].count('w'),
        'draw': team['result'].count('d'),
        'lose': team['result'].count('l'),
    }

def calculate_score(team):
    score = (team['win'] * 3) + team['draw']
    team['score'] = score
    return team

print('--------------------')

def check_score(team):
    return team['score'] >= 50

print('--------------------')

# map()

# tmp_score_board = list()
# for team in teams:
#    tmp_score_board.append(parse_result(team))
tmp_score_board = list(map(parse_result, teams))


print('--------------------')

# map()
# lambda

# score_board = list()
# for team in tmp_score_board:
#     score_board.append(calculate_score(team))
score_board = list(map(calculate_score, tmp_score_board))


score_board = list(map(calculate_score, tmp_score_board))

print('--------------------')



# for team in score_board:
#     print(team)


print('--------------------')

# filter()
# lambda

# passed_teams = list()
# for team in score_board:
#     if check_score(team):
#         passed_teams.append(team)


# passed_teams = filter(check_score, score_board) # functons -> variblse
passed_teams = list(filter(lambda t: t['score'] >=50, score_board)) 

print('--------------------')


score_board = sorted(
    score_board, key=lambda x : x['score'],
    reverse=True
    ) 

for index, team in enumerate(score_board):
    print( index+1 , team)


