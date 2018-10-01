import sys
import os
import Dao


queenNumber = 8
solutions =[]

# función recursiva
def find_solution(column, columns,lowerDiagonal, higherDiagonal):
    if column == queenNumber:
        # Guarda los datos en BD
        Dao.add_solution(solutions)    
    else:
        for j in range(1,queenNumber+1):
            # Si no esta en ninguna fila, columna o diagonal
            if not j in columns and not j-column in lowerDiagonal and not j+column in higherDiagonal:
                solutions[column] = j
                columns.append(j),lowerDiagonal.append(j-column),higherDiagonal.append(j+column)
                find_solution(column+1, columns,lowerDiagonal,higherDiagonal)
                columns.pop(), lowerDiagonal.pop(),higherDiagonal.pop()

def get_solution(number):
    # Elimina los datos anteriores de la BD
    Dao.romove_results()
    global queenNumber 
    global solutions 
    queenNumber =   number    
    solutions= [None]*queenNumber
    find_solution(0,[],[],[])
    numberSolution = Dao.get_solutions_number(queenNumber)
    # Imprime el número de soluciones
    print(str(numberSolution)+" soluciones")
    return numberSolution

def main(argv = None):        
    number = 8
    if len(argv) > 1:        
        number= int(argv[1])
    get_solution(number)  
    os._exit(1)     

if __name__ == "__main__":
    sys.exit(main(sys.argv))
