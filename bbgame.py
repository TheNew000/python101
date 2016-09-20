import player_class

players = [
  {
    'name': 'Paul Millsap',
    'position': 'PF',
    'avgMinutesPlayed': 36,
    'avgPoints': 16.4,
    'avgRebounds': 9.4,
    'starter': True
  },
  {
    'name': 'Jeff Teague',
    'position': 'PG',
    'avgMinutesPlayed': 28.6,
    'avgPoints': 15.6,
    'avgRebounds': 1.9,
    'starter': True
  },
  {
    'name': 'Al Horford',
    'position': 'C',
    'avgMinutesPlayed': 32,
    'avgPoints': 13.2,
    'avgRebounds': 6.8,
    'starter': True
  },
  {
    'name': 'Kent Bazemore',
    'position': 'SF',
    'avgMinutesPlayed': 31.8,
    'avgPoints': 12,
    'avgRebounds': 6.6,
    'starter': True
  },
  {
    'name': 'Kyle Korver',
    'position': 'SG',
    'avgMinutesPlayed': 32.4,
    'avgPoints': 11.2,
    'avgRebounds': 4.9,
    'starter': True
  },
  {
    'name': 'Dennis Schroder',
    'position': 'PG',
    'avgMinutesPlayed': 18.3,
    'avgPoints': 10.7,
    'avgRebounds': 1.8,
    'starter': False
  },
  {
    'name': 'Kris Humphries',
    'position': 'PF',
    'avgMinutesPlayed': 14.7,
    'avgPoints': 9.7,
    'avgRebounds': 5.7,
    'starter': False
  },
  {
    'name': 'Mike Scott',
    'position': 'PF',
    'avgMinutesPlayed': 17.6,
    'avgPoints': 7.0,
    'avgRebounds': 3.6,
    'starter': False
  },
  {
    'name': 'Thabo Sefolosha',
    'position': 'SF',
    'avgMinutesPlayed': 18.9,
    'avgPoints': 4.8,
    'avgRebounds': 3.9,
    'starter': False
  },
  {
    'name': 'Mike Muscala',
    'position': 'PF',
    'avgMinutesPlayed': 7.4,
    'avgPoints': 2.7,
    'avgRebounds': 1.9,
    'starter': False
  },
  {
    'name': 'Tim Hardaway Jr.',
    'position': 'SG',
    'avgMinutesPlayed': 9.7,
    'avgPoints': 2.2,
    'avgRebounds': 1.0,
    'starter': False
  },
  {
    'name': 'Lamar Patterson',
    'position': 'SG',
    'avgMinutesPlayed': 5.0,
    'avgPoints': 1.5,
    'avgRebounds': 1.3,
    'starter': False
  },
  {
    'name': 'Kirk Hinrich',
    'position': 'SG',
    'avgMinutesPlayed': 4.5,
    'avgPoints': 0.8,
    'avgRebounds': 0.7,
    'starter': False
  }
]

# newPlayers = []
#     newPlayers.append(player_class.Player(player['name'], player['position'], player['avgMinutesPlayed'], player['avgPoints'], player['avgRebounds'], player['starter']))

time_li = []
avg_st_time = []
avg_b_time = []
player_name = []
top_player = []
top_rebound = []
avg_pts = []
temp = 0
best_player = ''
for player in players:
    for key, value in player.items():
        if key == 'avgMinutesPlayed':
            time_li.append(value)
        if key == 'avgMinutesPlayed' and player['starter']:
            avg_st_time.append(player[key])
        if key == 'avgMinutesPlayed' and not player['starter']:
            avg_b_time.append(player[key])
    player_name.append(player['name'])
    if player['avgPoints'] > 10:
        top_player.append(player['name'])
    if player['avgRebounds'] > 5:
        top_rebound.append(player['name'])
    this_player = player['avgPoints']/player['avgMinutesPlayed']
    if this_player > temp:
        best_player = player['name']
    avg_pts.append(player['avgPoints'])

print 'Average Player Playing Time:',sum(time_li)/len(time_li)
print 'Average Starter Playing Time:',sum(avg_st_time)/len(avg_st_time)
print 'Average Bench Playing Time:',sum(avg_b_time)/len(avg_b_time)
print 'Player Names:', player_name
print 'Top Scoring Players:',top_player
print 'Top Rebounding Players:',top_rebound
print 'Most Points Per Minute:', best_player
print 'Average Points Scored by Team:', sum(avg_pts)/len(avg_pts)
