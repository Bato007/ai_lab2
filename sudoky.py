m, n = None, None
boxSize = 3

def read_file(filename):
  file = open(filename, 'r')
  fileLines = file.readlines()
  for index, line in enumerate(fileLines):
    global n, m, sudoku, boxSize
    
    if index == 0:
      n = line
      n.rstrip("\n")
    elif index == 1:
      m = line
      m.rstrip("\n")
      sudoku = [[0 for i in range(int(n))] for j in range(int(m))]
    else:
      values = line.split(" ")
      if not values == None:
        sudoku [int(values[0])][int(values[1])] = int(values[2].rstrip("\n"))
    
    if (int(n) % 2 == 0):
      boxSize = 2


# Se encuentra el siguiente espacio vacio
def find_empty_location(arr, l):
  for row in range(len(sudoku)):
    for col in range(len(sudoku[0])):
      if(arr[row][col]== 0):
        l[0]= row
        l[1]= col
        return True
  return False

# Se chequea si el numero ya existe en la fila
def used_in_row(arr, row, num):
	for i in range(len(sudoku)):
		if(arr[row][i] == num):
			return True
	return False

# Se chequea si el numero ya existe en la columna
def used_in_col(arr, col, num):
	for i in range(len(sudoku[0])):
		if(arr[i][col] == num):
			return True
	return False

# Se chequea si existe en la caja
def used_in_box(arr, row, col, num):
  global boxSize
  for i in range(boxSize):
    for j in range(boxSize):
      if(arr[i + row][j + col] == num):
        return True
  return False

# Se chequea si se puede utilizar el numero
def check_location_is_safe(arr, row, col, num):
  global boxSize
  # Se chequea que la fila, columna y cajita no contengan el numero
  return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % boxSize, col - col % boxSize, num)

# Se intenta colocar valores en todos los espacios vacios
def solve_sudoku(arr):
	# Lista que lleva la fila y columna actual
	l =[0, 0]
	
	# Se chequea si la ubicacion actual esta vacia "0"
	if(not find_empty_location(arr, l)):
		return True
	
	# Se obtiene la fila y columna a utilizar
	row, col = l
	
	# Se obtienen los numeros del 1 al 9
	for num in range(1, 10):
		
		# if looks promising
		if(check_location_is_safe(arr,
						row, col, num)):
			
			# make tentative assignment
			arr[row][col]= num

			# return, if success,
			# ya !
			if(solve_sudoku(arr)):
				return True

			# failure, unmake & try again
			arr[row][col] = 0
			
	# this triggers backtracking	
	return False



read_file("file.txt")
if(solve_sudoku(sudoku)):
  print("La solucion para el sudoku es")
  print(sudoku)
else:
  print("No existe solucion para el sudoku ingresado")
