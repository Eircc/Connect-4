import pygame
import sys
# import math

class Connect4:
	def __init__(self) -> None:
		pygame.init()
		
		self.WIDTH = 700
		self.HEIGHT = 700
		self.SIZE = (self.WIDTH, self.HEIGHT)

		self.screen = pygame.display.set_mode(self.SIZE)

		self.running = True

		# set window name
		pygame.display.set_caption("Connect 4")

		self.clock = pygame.time.Clock()
		self.FPS = 60

		# colours
		self.WHITE = (255, 255, 255)
		self.BLACK = (0, 0, 0)
		self.YELLOW = (255, 230, 80)
		self.RED = (255, 0, 0)
		self.BLUE = (0, 0, 255)
	
		self.board = [ # board 7 wide 6 tall
			[0, 0, 0, 0, 0, 0, 0], # 0 for empty, 1 for red, 2 for yellow
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
		]

		self.turn = 2 # 1 for red, 2 for yellow

	def display(self):
		self.screen.fill(self.BLACK)
		pygame.draw.rect(self.screen, self.BLUE, pygame.Rect(0, 100, 700, 600))
		for r in range(6): # rows
			for c in range(7): # cols
				if self.board[r][c] == 0:
					colour = self.BLACK
				elif self.board[r][c] == 1:
					colour = self.RED
				else: 
					colour = self.YELLOW
				pygame.draw.ellipse(self.screen, colour, (c * 100 + 5, (r + 1) * 100 + 5, 90, 90))
		x = pygame.mouse.get_pos()[0]
		if x < 45:
			x = 45
		if x > 655:
			x = 655
		if self.turn == 1:
			colour = self.RED
		else:
			colour = self.YELLOW
		pygame.draw.ellipse(self.screen, colour, (x - 45, 5, 90, 90))
		pygame.display.update()

	def find_row(self, col):
		drop = -1
		for i in range(5, -1, -1):
			if self.board[i][col] == 0:
				drop = i
				break
		return drop

	def check_win(self, row, col): 
		win = False

		# check horizontal
		if col == 0:
			if self.board[row][col + 1] == self.board[row][col + 2] and self.board[row][col + 2] == self.board[row][col + 3] and self.board[row][col + 1] == self.turn:
				return True
		elif col == 1:
			if self.board[row][col + 1] == self.board[row][col + 2] and self.board[row][col + 1] == self.turn:
				if self.board[row][col - 1] == self.turn or self.board[row][col + 3] == self.turn:
					return True
		elif col == 2:
			if self.board[row][col + 1] == self.turn:
				if self.board[row][col + 2] == self.board[row][col + 3] and self.board[row][col + 2] == self.turn:
					return True
				elif self.board[row][col - 1] == self.turn:
					if self.board[row][col - 2] == self.turn or self.board[row][col + 2] == self.turn:
						return True
		elif col == 3:
			if self.board[row][col - 3] == self.board[row][col - 2] and self.board[row][col - 2] == self.board[row][col - 1] and self.board[row][col - 1] == self.turn:
				return True
			elif self.board[row][col - 2] == self.board[row][col - 1] and self.board[row][col - 1] == self.board[row][col + 1] and self.board[row][col + 1] == self.turn:
				return True
			elif self.board[row][col - 1] == self.board[row][col + 1] and self.board[row][col + 1] == self.board[row][col + 2] and self.board[row][col + 2] == self.turn:
				return True
			elif self.board[row][col + 1] == self.board[row][col + 2] and self.board[row][col + 2] == self.board[row][col + 3] and self.board[row][col + 3] == self.turn:
				return True
		elif col == 4:
			if self.board[row][col - 1] == self.turn:
				if self.board[row][col - 2] == self.board[row][col - 3] and self.board[row][col - 3] == self.turn:
					return True
				elif self.board[row][col + 1] == self.turn:
					if self.board[row][col - 2] == self.turn or self.board[row][col + 2] == self.turn:
						return True
		elif col == 5:
			if self.board[row][col - 1] == self.board[row][col - 2] and self.board[row][col - 2] == self.turn:
				if self.board[row][col - 3] == self.board or self.board[row][col + 1] == self.turn:
					return True
		else:
			if self.board[row][col - 1] == self.board[row][col - 2] and self.board[row][col - 2] == self.board[row][col - 3] and self.board[row][col - 3] == self.turn:
				return True

		# check vertical

		# 0, middle
		# 1, middle, 1 down
		# 2, middle, 2 down
		# 3, 3 down
		# 4, 2 down
		# 5, 1 down

		if row == 0:
			pass
		elif row == 1:
			pass
		elif row == 2:
			pass
		elif row == 3:
			pass
		elif row == 4:
			pass
		else:
			pass

		# check diagonal

	def check_event(self, event):
		# user is quitting the game
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			x = pygame.mouse.get_pos()[0]
			col = x // 100
			row = self.find_row(col)
			if row != -1:
				self.board[row][col] = self.turn
				self.check_win(row, col)
				if self.turn == 1:
					self.turn = 2
				else:
					self.turn = 1

	def on_execute(self):
		while self.running:
			self.display()
			for event in pygame.event.get():
				self.check_event(event)

start = Connect4()
start.on_execute()