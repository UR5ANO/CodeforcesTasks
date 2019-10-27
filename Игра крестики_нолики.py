lines = [
	[0, 4, 8],
	[2, 4, 6],
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
]


def count_line(field, line):
	c = {
		' ': 0,
		'X': 0,
		'O': 0,
	}
	for e in line:
		s = field[e // 3][e % 3]
		c[s] += 1
	return c


def print_field(f):
	tabs = 7
	print('-' * tabs)
	for i in range(3):
		print('|' + '|'.join(f[i]) + '|')
		print('-' * tabs)


def can_move(field, move):
	move = int(move) - 1
	if field[move // 3][move % 3] != ' ':
		return False
	else:
		return True


def get_input(field):
	move = input("Your turn: 1-9: ")
	while (
		len(move) != 1 or 
		move not in list(map(str, range(1, 10))) or
		not can_move(field, move)
	):
		move = input("Incorrect input! Your turn: 1-9: ")
	return int(move) - 1


def do_move(field, move, player):
	i = move // 3
	j = move % 3
	field[i][j] = player


def comp_move(field):

	for line in lines:
		c = count_line(field, line)
		if c['O'] == 2 and c[' '] == 1:
			for e in line:
				if field[e // 3][e % 3] == ' ':
					do_move(field, e, 'O')
					return

	for line in lines:
		c = count_line(field, line)
		if c['X'] == 2 and c[' '] == 1:
			for e in line:
				if field[e // 3][e % 3] == ' ':
					do_move(field, e, 'O')
					return

	profit = {}
	for i in range(9):
		if field[i // 3][i % 3] != ' ':
			continue
		for line in lines:
			if i not in line:
				continue
			c = count_line(field, line)
			if c['X'] == 0:
				if i not in profit:
					profit[i] = 0
				profit[i] += c['O'] + 1
			elif c['O'] == 0:
				if i not in profit:
					profit[i] = 0
				profit[i] += c['X']
	if len(profit):
		best_move = max(profit.items(), key=lambda x: x[1])[0]
		do_move(field, best_move, 'O')
		return

	for i in range(3):
		for j in range(3):
			if field[i][j] == ' ':
				do_move(field, 3 * i + j, 'O')
				return


def game_over(field):

	all_filled = True
	for i in range(3):
		for j in range(3):
			if field[i][j] == ' ':
				all_filled = False
	if all_filled:
		return ' '

	for line in lines:
		c = count_line(field, line)
		if c['X'] == 3:
			return 'X'
		if c['O'] == 3:
			return 'O'
	return None


def game(field):
	while True:
		print_field(field)
		move = get_input(field)
		do_move(field, move, 'X')
		w = game_over(field)
		if w is not None:
			if w == 'X':
				print("You win!")
				break
			else:
				print("Draw!")
				break
		comp_move(field)
		w = game_over(field)
		if w is not None:
			if w == 'O':
				print("You lose!")
				break
			else:
				print("Draw!")
				break
		print_field(field)
	print_field(field)


field = [
	[' ', ' ', ' '],
	[' ', ' ', ' '],
	[' ', ' ', ' ']
]

game(field)
