import time

def is_num(number):
	try:
		int(number)
		return True
	except ValueError:
		return False

def create_decks(list):
	
	decks = []
	player = 0
	
	for x in list:

		if "Player" in x:
			decks.append([])
			player += 1

		elif is_num(x):
			decks[player-1].append(int(x))
			

	return decks
	
def start_round(decks, recursion_mode = False):
	print "ONE"
	cards = []
	recurse = True
	time.sleep(0.1)
	
	for p in decks:
		cards.append(p.pop(0))
		if len(p) < cards[-1]: recurse = False
	
	if recurse and recursion_mode:
		sub_decks = [decks[i][0:cards[i]] for i in range(len(decks))]
		winner, _ = start_recursive_combat_game(sub_decks)
		decks[winner].append(cards.pop(winner))
		decks[winner].extend(cards)
		return decks
	
	decks[cards.index(max(cards))].extend(sorted(cards, reverse=True))
	return decks

def start_combat_game(decks):
	print "TWO"
	
	
	while True:
		print "THREE"
		if min([len(x) for x in decks]) == 0: break
		decks = start_round(decks)
	
	winner = [len(x) for x in decks].index(max([len(x) for x in decks]))
	return winner, decks

def start_recursive_combat_game(decks):
	print "FOUR"
	
	prev_decks = set()
	
	while True:
		print "FIVE"
		if min([len(x) for x in decks]) == 0: break
		if decks[0] in prev_decks and decks[1] in prev_decks: return 0, decks
		decks = start_round(decks, True)
		
		decks_config = (tuple(decks[0]), tuple(decks[1]))
		prev_decks.add(decks_config) 
	
	winner = [len(x) for x in decks].index(max([len(x) for x in decks]))
	return winner, decks
	
def count_points(winner, game):
	
	points = 0
	multiplier = 1
	
	for x in range(len(game[winner])):
		points += game[winner].pop() * multiplier
		multiplier += 1

	return points

if __name__ == "__main__":
	
	file = open('input-22.txt', 'r')
	
	list = file.readlines()
	list = [x.strip() for x in list]

	# decks = create_decks(list)
	# winner, game = start_combat_game(decks)
	# points = count_points(winner, game)
	# print points
	
	decks = create_decks(list)
	recursion_winner, recursion_game = start_recursive_combat_game(decks)
	recursion_points = count_points(recursion_winner, recursion_game)
	print recursion_points

	
	