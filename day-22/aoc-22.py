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
	
def start_round(decks):
	
	cards = []
	for p in decks:
		cards.append(p.pop(0))
	
	decks[cards.index(max(cards))].extend(sorted(cards, reverse=True))
	
	return decks	

def start_combat_game(decks):
	
	while True:
		if min([len(x) for x in decks]) == 0: break
		decks = start_round(decks)
		
	return decks
	
def count_points(game):
	
	winner = [len(x) for x in game].index(max([len(x) for x in game]))
	
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

	decks = create_decks(list)
	game = start_combat_game(decks)
	points = count_points(game)

	print points
	
	