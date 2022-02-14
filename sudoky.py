m, n = None, None

def read_file(filename):
  file = open(filename, 'r')
  fileLines = file.readlines()
  for index, line in enumerate(fileLines):
    global n, m, sudoku
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


read_file("file.txt")
print(sudoku)