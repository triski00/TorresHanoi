from pilaHanoi import Pila

def getTablero(n):
    pila1 = Pila()
    pila2 = Pila()
    pila3 = Pila()
    for disco in range(n, 0, -1):
        pila1.push(disco)
    return (pila1, pila2, pila3)

def solve(tablero, n, origen, auxiliar, destino, movimientos):
    if n == 1:
        disco = origen.pop()
        destino.push(disco)
        movimientos.append(f"D{disco} from T{origen} to T{destino}")
    else:
        solve(tablero, n-1, origen, destino, auxiliar, movimientos)
        disco = origen.pop()
        destino.push(disco)
        movimientos.append(f"D{disco} from T{origen} to T{destino}")
        solve(tablero, n-1, auxiliar, origen, destino, movimientos)

if __name__ == "__main":
    n = 5  # Número de discos
    tablero = getTablero(n)
    print("Estado inicial del tablero:")
    print(f"T1: {tablero[0]}\nT2: {tablero[1]}\nT3: {tablero[2]}")
    
    movimientos = []
    solve(tablero, n, tablero[0], tablero[1], tablero[2], movimientos)
    
    print("\nLista de movimientos:")
    for movimiento in movimientos:
        print(movimiento)
    
    print("\nEstado final del tablero:")
    print(f"T1: {tablero[0]}\nT2: {tablero[1]}\nT3: {tablero[2]}")
