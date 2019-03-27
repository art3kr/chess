'''
Chess game to practice opening lines

Created by: Antonio Trani
Email: art3kr@virginia.edu
Date Created: 3/15/19

Edits:

1.1 - 3/19/19:
	- Added GUI Functions


'''

##Libraries to import:
import pygame
import threading
import sys

#---------------------##Classes----------------------------------#
class Piece:
	def __init__(self,piece_info,board_pos_coord):

		self.piece_info = piece_info
		self.board_pos_coord = board_pos_coord

		color = piece_info[0]
		piece_type = piece_info[1]

		##Color
		#White
		if color == 'w':
			y_image_loc = -1

		#Black
		elif color == 'b':
			y_image_loc = square_height

		##Pieces
		#Rook
		if piece_type == 'R':
			x_image_loc = 4*square_width

		#Knight
		elif piece_type == 'N':
			x_image_loc = 3*square_width

		#Bishop
		elif piece_type == 'B':
			x_image_loc = 2*square_width

		#King
		elif piece_type == 'K':
			x_image_loc = -1

		#Queen
		elif piece_type == 'Q':
			x_image_loc = 1*square_width

		#Pawn
		elif piece_type == 'P':
			x_image_loc = 5*square_width

		self.color = color
		self.piece_type = piece_type

		self.image_subsection = (x_image_loc,y_image_loc,square_width,square_height)

		self.pixel_pos = (0,0)

	def get_board_pos_coord(self):
		return self.board_pos_coord

	def set_pixel_pos(self,pixel_pos):
		self.pixel_pos = pixel_pos

	def set_board_pos_coord(self,board_pos_coord):
		self.board_pos_coord = board_pos_coord



#---------------------##GUI Functions----------------------------#

##Create Pieces
#Return list of active pieces
def create_pieces(board):

	list_of_active_pieces = []

	row_count = -1
	for row in board:

		row_count += 1
		column_count = -1

		for column in row:
			column_count += 1

			if type(column) == str:

				piece = Piece(column,[row_count,column_count])

				list_of_active_pieces.append(piece)

	return list_of_active_pieces

##Convert board pixel coordinates to board position coordinates
#Return board pixel coordinates
def convert_board_pixel_coord_to_pos(board_pixel_coord):
	x_coord = board_pixel_coord[0]
	y_coord = board_pixel_coord[1]

	row = y_coord//square_width
	column = x_coord//square_width

	return [int(row),int(column)]


##Convert initial board position coordinates to board pixel coordinates for where to place pieces on board
#Return board image coordinates
def convert_board_pos_to_pixel_coord(board_pos_coord):
	
	row = board_pos_coord[0]
	column = board_pos_coord[1]

	#Row
	if row == 0:
		y_dest_board = -1

	else:
		y_dest_board = row * square_width

	#Column
	if column == 0: 
		x_dest_board = -1

	else:
		x_dest_board = column * square_width

	return (x_dest_board, y_dest_board)

##Draw board and pieces
def draw_all(list_of_active_pieces):

	screen.blit(board_image,(0,0))

	draw_pieces(list_of_active_pieces)


##Draw the pieces on the board
def draw_pieces(list_of_active_pieces):

	for piece in list_of_active_pieces:

		image_subsection = piece.image_subsection
		

		if piece.pixel_pos == (0,0):

			(x_dest_board, y_dest_board) = convert_board_pos_to_pixel_coord(piece.board_pos_coord)
			screen.blit(pieces_image,(x_dest_board,y_dest_board),image_subsection)

		else:
			screen.blit(pieces_image,piece.pixel_pos,image_subsection)


##Get the piece in the occupied space by the active piece list
#Return piece class
def get_piece_from_list_by_coord(board_pos_coord):

	for piece in list_of_active_pieces:
		if piece.board_pos_coord == board_pos_coord:
			return piece

##Get the piece in the occupied space by the board
#Return piece str
def get_piece_from_board_by_coord(space,board):

	row = space[0]
	column = space[1]

	piece = board[row][column]

	return piece

##Find if space is occupied
#Return is_occupied bool
def is_space_occupied(space,board):

	piece = get_piece_from_board_by_coord(space,board)

	if piece == 0:

		is_occupied = False

	elif piece != 0:

		is_occupied = True

	return is_occupied

##Find if space is occupied by piece owned by player
#Return is_occupied_by_player bool
def is_space_occupied_by_players_piece(space,board):

	piece = get_piece_from_board_by_coord(space,board)

	is_occupied_by_player = False

	if is_space_occupied(space,board) == True:
		if piece[0] == player_side:
			is_occupied_by_player = True
		

	return is_occupied_by_player


##Find if space is occupied by piece owned by opponent
#Return is_occupied_by_opponent bool
def is_space_occupied_by_opponent_piece(space,board):

	piece = get_piece_from_board_by_coord(space,board)

	is_occupied_by_opponent = False

	if is_space_occupied(space,board) == True:
		if piece[0] != player_side:
			is_occupied_by_opponent = True
		

	return is_occupied_by_opponent

##Update the 2D board matrix
#Returns board
def update_board(board,old_board_pos_coord,new_board_pos_coord):

	board[new_board_pos_coord[0]][new_board_pos_coord[1]] = board[old_board_pos_coord[0]][old_board_pos_coord[1]]

	board[old_board_pos_coord[0]][old_board_pos_coord[1]] = 0

	return board

def find_possible_moves(piece,board):
	pass

##Checking to see if pieces are in the way of the move the player is attempting to make
#Returns is_piece_in_way_of_move
def is_piece_in_way_of_move(piece,board,new_board_pos_coord):

	current_board_pos_coord = piece.get_board_pos_coord()

	is_piece_in_way_of_move = True

	if piece.piece_type == 'R':
		#Moving in x direction
		if current_board_pos_coord[0] == new_board_pos_coord[0]:
			#Moving to the right on the board
			if current_board_pos_coor[1] > new_board_pos_coord[1]
			for x_value in range(current_board_pos_coord[1],new_board_pos_coord[1]):
				print(x_value)
				space_to_check = [current_board_pos_coord[0],x_value]

				if is_space_occupied(space_to_check,board) == False:
					is_piece_in_way_of_move = False

		#Moving in y direction
		elif current_board_pos_coord[1] == new_board_pos_coord[1]:
			for y_value in range(current_board_pos_coord[0],new_board_pos_coord[0]):
				print(y_value)
				space_to_check = [y_value,current_board_pos_coord[1]]

				if is_space_occupied(space_to_check,board) == False:
					is_piece_in_way_of_move = False

		is_piece_in_way_of_move = False

	elif piece.piece_type == 'N':

		is_piece_in_way_of_move = False

	elif piece.piece_type == 'B':
		pass

	elif piece.piece_type == 'Q':
		pass

	elif piece.piece_type == 'K':
		pass

	elif piece.piece_type == 'P':
		pass

	return is_piece_in_way_of_move

##Makes move by updating piece position info and board info
def make_move(piece,board,new_board_pos_coord):

	if is_valid_move(piece,board,new_board_pos_coord) == True:
		old_position = piece.get_board_pos_coord()
		print(old_position,new_board_pos_coord)  #Debug
		piece.set_pixel_pos((0,0))
		piece.set_board_pos_coord(new_board_pos_coord)
		board = update_board(board,old_position,new_board_pos_coord)

	elif is_valid_move(piece,board,new_board_pos_coord) == False:
		piece.set_pixel_pos((0,0))

##Checks if the move can be made
#Returns is_valid_move
def is_valid_move(piece,board,new_board_pos_coord):

	print(piece.piece_type) #Debug

	is_valid_move = False #Debug

	if is_space_occupied_by_players_piece(new_board_pos_coord,board) == True:
		is_valid_move = False

	elif is_space_occupied_by_opponent_piece(new_board_pos_coord,board) == True:

		if is_valid_capture(piece,board,new_board_pos_coord) == False:
			is_valid_move = False

		elif is_valid_capture(piece,board,new_board_pos_coord) == True:
			is_valid_move = True

	else:

		current_board_pos_coord = piece.get_board_pos_coord()

		if piece.piece_type == 'R':
			if current_board_pos_coord[0] != new_board_pos_coord[0] and current_board_pos_coord[1] != new_board_pos_coord[1]:
				is_valid_move = False
			else:
				if is_piece_in_way_of_move(piece,board,new_board_pos_coord) == True:
					is_valid_move = False
				elif is_piece_in_way_of_move(piece,board,new_board_pos_coord) == False:
					is_valid_move = True

		elif piece.piece_type == 'N':

			pass			

		elif piece.piece_type == 'B':
			if current_board_pos_coord[0] == new_board_pos_coord[0] or current_board_pos_coord[1] == new_board_pos_coord[1]:
				is_valid_move = False
			else:
				if is_piece_in_way_of_move(piece,board,new_board_pos_coord) == True:
					is_valid_move = False
				elif is_piece_in_way_of_move(piece,board,new_board_pos_coord) == False:
					is_valid_move = True

		elif piece.piece_type == 'Q':
			pass

		elif piece.piece_type == 'K':
			pass

		elif piece.piece_type == 'P':
			pass

		# is_valid_move = True


	return is_valid_move


##Checks if the move to capture is valid
#Returns is_valid_capture
def is_valid_capture(piece,board,new_board_pos_coord):

	defending_piece = get_piece_from_board_by_coord(new_board_pos_coord,board)

	if defending_piece[1] == 'K':
		is_valid_capture = False

	else:
		is_valid_capture = True

	if is_valid_capture == True:
		move_piece_to_captured_list(new_board_pos_coord)

	return is_valid_capture

##Appends captured piece to captured piece list
def move_piece_to_captured_list(new_board_pos_coord):

	captured_piece = remove_piece_from_active_list(new_board_pos_coord)
	list_of_captured_pieces.append(captured_piece)

##Pops captured piece from active piece list - must be called inside move_piece_to_captured_list
#Returns captured piece class
def remove_piece_from_active_list(new_board_pos_coord):

	for index, piece in enumerate(list_of_active_pieces):
		if piece.board_pos_coord == new_board_pos_coord:
			captured_piece = list_of_active_pieces.pop(index)

			return captured_piece



#---------------------##Initial Conditions--------------------------#

##Condition to end game
game_over = False

player_side = 'w'

##Castling rights
white_castled = False
black_castled = False

##Captured pieces list
list_of_captured_pieces = []

##Condition to check if a piece is being dragged
is_dragging = False

##Function to initialize board
def initial_board():

	if player_side == 'w':
		board = [
		['bR','bN','bB','bQ','bK','bB','bN','bR'],
		['bP','bP','bP','bP','bP','bP','bP','bP'],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		['wP','wP','wP','wP','wP','wP','wP','wP'],
		['wR','wN','wB','wQ','wK','wB','wN','wR']
		]
	elif player_side == 'b':
		board = [
		['wR','wN','wB','wQ','wK','wB','wN','wR'],
		['wP','wP','wP','wP','wP','wP','wP','wP'],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		[0   ,   0,   0,   0,   0,   0,   0,   0],
		['bP','bP','bP','bP','bP','bP','bP','bP'],
		['bR','bN','bB','bK','bQ','bB','bN','bR']
		]
		
	return board

#---------------------##MAIN Stuff--------------------------#
##Start PyGame:
pygame.init()

##Load screen:
screen = pygame.display.set_mode((1000,1000))

##Load images:
board_image = pygame.image.load('Media\\board.png').convert()
pieces_image = pygame.image.load('Media\\Chess_Pieces_Sprite.png').convert_alpha()

##Get sizes:
size_of_board_image = board_image.get_rect().size
#Get size of the individual squares
square_width = size_of_board_image[0]/8
square_height = size_of_board_image[1]/8


##Resize images
pieces_image = pygame.transform.scale(pieces_image,(int(square_width*6),int(square_height*2)))

##Set windows as same size of background, load background image
screen = pygame.display.set_mode(size_of_board_image) 

##Load caption:
pygame.display.set_caption("Chess Game")

#---------------------##Blit/Draw initial images-------------------------#
screen.blit(board_image,(0,0))
board = initial_board()
list_of_active_pieces = create_pieces(board)
draw_pieces(list_of_active_pieces)
pygame.display.update()


##-----------------------Main infinite loop---------------------------#
while game_over == False:
	pygame.display.update()

	# event = pygame.event.poll()

	##Get in-game events (mouse clicks, etc.)
	for event in pygame.event.get():

		##If user clicks the X button to leave the game
		if event.type == pygame.QUIT:
			game_over = True
			# pygame.quit()
			# sys.exit()

		##If the user clicks the mouse
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_position = pygame.mouse.get_pos()
			mouse_position_as_coord = convert_board_pixel_coord_to_pos(mouse_position)

			# find_possible_moves()


			if is_space_occupied_by_players_piece(mouse_position_as_coord,board) == True:
				dragging_piece = get_piece_from_list_by_coord(mouse_position_as_coord)
				is_dragging = True

		elif event.type == pygame.MOUSEBUTTONUP and is_dragging == True:
			is_dragging = False

			mouse_position = pygame.mouse.get_pos()
			mouse_position_as_coord = convert_board_pixel_coord_to_pos(mouse_position)

			make_move(dragging_piece,board,mouse_position_as_coord)


	if is_dragging == True:

		mouse_position = pygame.mouse.get_pos()
		dragging_piece.set_pixel_pos((mouse_position[0]-square_width/2,mouse_position[1]-square_width/2))

	draw_all(list_of_active_pieces)
