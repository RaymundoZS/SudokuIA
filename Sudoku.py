def solve_sudoku(board):
    """
    Resuelve el Sudoku dado utilizando un algoritmo de búsqueda recursiva con backtracking.
    
    Args:
    - board: Una lista de listas que representa el tablero de Sudoku. Cada list                                                                                                                                                     a interna representa una fila del tablero,
    y cada elemento de la lista representa un número en la fila. Los espacios vacíos están representados por el valor 0.
             
    Returns:
    - True si el Sudoku fue resuelto, False en caso contrario.
    """
    
    # Encontrar la próxima casilla vacía en el tablero.
    row, col = find_empty_cell(board)
    
    # Si no hay casillas vacías, el Sudoku está resuelto.
    if row is None or col is None:
        return True
    
    # Probar cada posible número en la casilla vacía.
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # Si el número es válido, colocarlo en la casilla y continuar con la búsqueda recursiva.
            board[row][col] = num
            if solve_sudoku(board):
                return True
            # Si no se puede resolver el Sudoku con esta configuración, retroceder y probar con otro número.
            board[row][col] = 0
            
    # Si no se puede resolver el Sudoku con ninguna configuración, el Sudoku no tiene solución.
    return False

def find_empty_cell(board):
    """
    Encuentra la próxima casilla vacía en el tablero de Sudoku.
    
    Args:
    - board: Una lista de listas que representa el tablero de Sudoku.
    
    Returns:
    - Una tupla que contiene la fila y la columna de la próxima casilla vacía en el tablero, o (None) si no hay más casillas vacías.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return (None, None)

def is_valid_move(board, row, col, num):
    """
    Comprueba si el número dado es válido en la casilla dada.
    
    Args:
    - board: Una lista de listas que representa el tablero de Sudoku.
    - row: La fila de la casilla.
    - col: La columna de la casilla.
    - num: El número que se quiere colocar en la casilla.
    
    Returns:
    - True si el número es válido en la casilla dada, False en caso contrario.
    """
    
    # Comprobar si el número ya aparece en la misma fila, columna o región.
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[(row//3)*3 + i//3][(col//3)*3 + i%3] == num:
            return False
        
    return True

def read_sudoku_file(file_name):
    """
    Lee un archivo de texto que contiene un tablero de Sudoku y lo convierte en una lista de listas de enteros.
    
    Args:
    - file_name: El nombre del archivo de texto que contiene el tablero de Sudoku.
    
    Returns:
    - Una lista de listas de enteros que representa el tablero de Sudoku, o None si no se puede leer el archivo.
    """
    
    try:
        with open(file_name, "r") as f:
            # Leer el contenido del archivo como una lista de cadenas de texto.
            lines = f.readlines()
            # Convertir cada cadena de texto en una lista de enteros.
            board = [[int(c) for c in line.strip()] for line in lines]
            return board
    except:
        # Si no se puede leer el archivo, devolver None.
        return None

# Aplicación de uso
file_name = "sudoku.txt"
board = read_sudoku_file(file_name)

if board is not None:
    if solve_sudoku(board):
        for row in board:
            print(row)
    else:
        print("El Sudoku no tiene solución.")
else:
    print("No se pudo leer el archivo.")