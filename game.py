import random
import copy

def checavizinhos(x, y, board):
	neighbors = 0
	execao = [-1, 0, 1]
	#for para lidar com celulas das bordas (com menos de 8 vizinhos)
	for i in execao:
		for j in execao:
			if (i == 0) and (j == 0):
				pass
			elif ((y + j) < 0) or ((y + j) > (25 - 1)):
				pass
			elif ((x + i) < 0) or ((x + i) > (25 - 1)):
				pass
			elif board[x + i][y + j] == 1:
				neighbors += 1
			else:
				pass
				
	return neighbors


def evolue(current_gen):
    #cria uma nova geracao a partir de uma copia da atual
	next_gen = copy.deepcopy(current_gen)
	
	for row in range(len(current_gen)):
		for col in range(len(next_gen[row])):
			num_neighbors = checavizinhos(row, col, current_gen)
		
			#determinando se a celula morre ou vive
			if (num_neighbors == 2) and (current_gen[row][col] == 1):
				next_gen[row][col] = 1
			elif num_neighbors == 3:
				next_gen[row][col] = 1
			elif num_neighbors < 2:
				next_gen[row][col] = 0
			else:
				next_gen[row][col] = 0

	return next_gen


def estadoinicial():
    first_gen = []

    for row in range(25):
        first_gen.append([])
        for column in range(25):
            #25% de chance de iniciar preenchida
            temp = random.randrange(0,4)
            if temp == 1:
                first_gen[row].append(1)
            else:
                first_gen[row].append(0)
    
    return first_gen