# Крестики-нолики ( текстовые )
import random

class TicTacToe():
	print("Крестики-нолики!")

	def mode_selection(self):
		answer = input("В какой режим хотите играть ai/pl? ")

		if answer == "ai":
			TicTacToe.vsAI().game()

		elif answer == "pl":
			TicTacToe.vsPlayer().game()

	# Игра против исскуственнго интеллекта
	class vsAI():
		def __init__(self, *kwargs):
				self.places = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
				self.cell = None
				self.rnd_token = random.randint(1, 2)

		def board_generation(self):
			print("")
			print(' -------------')

			for i in range(3):
				print(' |', self.places[ 0 + i * 3 ], '|', self.places[ 1 + i * 3 ], '|', self.places[ 2 + i * 3 ], '|')
				print(' -------------')

		def player_turn(self):
			print("")
			print('Ход игрока!')

			waiting = True
			if self.rnd_token == 1:
				token = "X"
			else:
				token = "O"

			while waiting:
				self.cell = input('Куда хотите поставить ' + token + ' ? ')

				try:
					self.cell = int(self.cell) 

				except:
					print("Вы должны ввести число.")
					continue

				if self.cell == 101:
					print("Секретный код 101, игра заканчивается!")
					break

				if self.cell >= 1 and self.cell <= 9:
					if str( self.places[ self.cell - 1 ] ) not in "XO":
						self.places[ self.cell - 1 ] = token
						waiting = False
					else:
						print("Эта клеточка уже занята.")

				else:
					print("Число должно быть от 1 до 9.")

		def AI_turn(self):
			print("")
			print("Ход бота!")

			running = True
			if self.rnd_token == 1:
				token = "O"
			else:
				token = "X"

			while running:
				
				rnd = random.choice(range(0, 9))

				if str( self.places[ rnd ] ) not in "XO":
					print("Бот ставит", self.places[ rnd ])
					self.places[ rnd ] = token
					running = False

		def check_win(self):
			self.win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), 
							  (0, 3, 6), (1, 4, 7), (2, 5, 8),
							  (0, 4, 8), (2, 4, 6))	

			for each in self.win_combo:
				if self.places[each[0]] == self.places[each[1]] == self.places[each[2]]:
					return self.places[each[0]]

			return False

		def game(self):
			turn = 0
			win = False

			while not win:

				self.board_generation()

				if self.rnd_token == 1:
					if turn % 2 == 0:
						self.player_turn()

						if self.cell == 101:
							break

					else:
						self.AI_turn()

				else:
					if turn % 2 == 0:
						self.AI_turn()

					else:
						self.player_turn()

						if self.cell == 101:
							break

				turn += 1

				if turn > 4:
					winner = self.check_win()
					if winner != False:
						print("Выйграл", winner, "!")
						win = True
						break

				if turn == 9:
					print("Ничья!")
					break

			self.board_generation()

			contin = input("Хотите продолжить yes/no? ")

			if contin == "yes":
				TicTacToe.vsAI().game()

	# Игра против человека
	class vsPlayer():
		def __init__(self, *kwargs):
				self.places = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
				self.cell = None
				self.rnd_token = random.randint(1, 2)

		def board_generation(self):
			print("")
			print(' -------------')

			for i in range(3):
				print(' |', self.places[ 0 + i * 3 ], '|', self.places[ 1 + i * 3 ], '|', self.places[ 2 + i * 3 ], '|')
				print(' -------------')

		def first_player_turn(self):
			print("")

			waiting = True
			if self.rnd_token == 1:
				token = "X"
			else:
				token = "O"

			print('Ход', token, 'игрока!')

			while waiting:
				self.cell = input('Куда хотите поставить ' + token + ' ? ')

				try:
					self.cell = int(self.cell) 

				except:
					print("Вы должны ввести число.")
					continue

				if self.cell == 101:
					print("Секретный код 101, игра заканчивается!")
					break

				if self.cell >= 1 and self.cell <= 9:
					if str( self.places[ self.cell - 1 ] ) not in "XO":
						self.places[ self.cell - 1 ] = token
						waiting = False
					else:
						print("Эта клеточка уже занята.")

				else:
					print("Число должно быть от 1 до 9.")

		def second_player_turn(self):
			print("")

			waiting = True
			if self.rnd_token == 1:
				token = "O"
			else:
				token = "X"

			print('Ход', token, 'игрока!')

			while waiting:
				self.cell = input('Куда хотите поставить ' + token + ' ? ')

				try:
					self.cell = int(self.cell) 

				except:
					print("Вы должны ввести число.")
					continue

				if self.cell == 101:
					print("Секретный код 101, игра заканчивается!")
					break

				if self.cell >= 1 and self.cell <= 9:
					if str( self.places[ self.cell - 1 ] ) not in "XO":
						self.places[ self.cell - 1 ] = token
						waiting = False
					else:
						print("Эта клеточка уже занята.")

				else:
					print("Число должно быть от 1 до 9.")

		def check_win(self):
			self.win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), 
							  (0, 3, 6), (1, 4, 7), (2, 5, 8),
							  (0, 4, 8), (2, 4, 6))	

			for each in self.win_combo:
				if self.places[each[0]] == self.places[each[1]] == self.places[each[2]]:
					return self.places[each[0]]		

			return False

		def game(self):
			turn = 0
			win = False

			while not win:

				self.board_generation()

				if self.rnd_token == 1:
					if turn % 2 == 0:
						self.first_player_turn()

						if self.cell == 101:
							break

					else:
						self.second_player_turn()

						if self.cell == 101:
							break

				else:
					if turn % 2 == 0:
						self.second_player_turn()

						if self.cell == 101:
							break

					else:
						self.first_player_turn()

						if self.cell == 101:
							break

				turn += 1

				if turn > 4:
					winner = self.check_win()
					if winner != False:
						print("Выйграл", winner, "!")
						win = True
						break

				if turn == 9:
					print("Ничья!")
					break

			self.board_generation()

			contin = input("Хотите продолжить yes/no? ")

			if contin == "yes":
				TicTacToe.vsPlayer().game()

if __name__ == '__main__':
	TicTacToe().mode_selection()