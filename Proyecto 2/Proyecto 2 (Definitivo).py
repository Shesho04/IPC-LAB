import string
import random

class Tablero:
    def __init__(self):
        self.tamaño = 10
        self.tablero = [[' ' for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        self.barcos = {'pequeño': 3, 'grande': 5}
    
    def imprimir_tablero(self, oculto=False):
        print('   ' + ' '.join(string.ascii_uppercase[:self.tamaño]))
        for i in range(self.tamaño):
            fila = ' '.join(self.tablero[i]) if not oculto else ' '.join([' ' if celda == 'S' else celda for celda in self.tablero[i]])
            print(f'{i+1:2d} {fila}')
    
    def es_posicion_valida(self, fila, columna):
        return 0 <= fila < self.tamaño and 0 <= columna < self.tamaño
    
    def colocar_barco(self, tipo_barco, pos_inicio, orientacion):
        longitud_barco = self.barcos[tipo_barco]
        fila, columna = pos_inicio
        if orientacion == 'horizontal':
            for i in range(longitud_barco):
                if not self.es_posicion_valida(fila, columna+i) or self.tablero[fila][columna+i] != ' ':
                    return False
            for i in range(longitud_barco):
                self.tablero[fila][columna+i] = 'S'
        else:  # orientacion == 'vertical'
            for i in range(longitud_barco):
                if not self.es_posicion_valida(fila+i, columna) or self.tablero[fila+i][columna] != ' ':
                    return False
            for i in range(longitud_barco):
                self.tablero[fila+i][columna] = 'S'
        return True
    
    def recibir_disparo(self, fila, columna):
        if not self.es_posicion_valida(fila, columna):
            return '¡Disparo inválido!'
        if self.tablero[fila][columna] == ' ':
            self.tablero[fila][columna] = 'O'  # Fallo
            return '¡Fallo!'
        if self.tablero[fila][columna] == 'S':
            self.tablero[fila][columna] = 'X'  # Impacto
            if self.verificar_barco_hundido():
                return '¡Impacto y barco hundido!'
            return '¡Impacto!'
        return '¡Ya se disparó allí!'
    
    def verificar_barco_hundido(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                if self.tablero[i][j] == 'S':
                    return False
        return True

def obtener_posicion_valida():
    while True:
        pos = input('Ingrese una posición (ejemplo: A1): ').upper()
        if len(pos) < 2 or len(pos) > 3:
            print('Posición inválida. Intente nuevamente.')
            continue
        columna = string.ascii_uppercase.index(pos[0])
        fila = int(pos[1:]) - 1
        if 0 <= columna < 10 and 0 <= fila < 10:
            return fila, columna
        print('Posición inválida. Intente nuevamente.')

def obtener_orientacion_valida():
    orientaciones = ['horizontal', 'vertical']
    while True:
        orientacion = input('Ingrese la orientación (horizontal o vertical): ')
        if orientacion.lower() in orientaciones:
            return orientacion.lower()
        print('Orientación inválida. Intente nuevamente.')

def colocar_barcos_jugador(tablero, jugador):
    print(f'Jugador {jugador}, coloca tus barcos:')
    for tipo_barco in ['pequeño', 'pequeño', 'pequeño', 'grande', 'grande']:
        while True:
            tablero.imprimir_tablero()
            print(f'Coloca un barco {tipo_barco}:')
            pos_inicio = obtener_posicion_valida()
            orientacion = obtener_orientacion_valida()
            if tablero.colocar_barco(tipo_barco, pos_inicio, orientacion):
                break
            print('No se puede colocar el barco ahí. Intente nuevamente.')
        print()

def jugar_batalla_naval():
    print('¡Bienvenido a Batalla Naval!')
    print('Cada jugador deberá colocar sus barcos en el tablero.')
    print('Luego, los jugadores se turnarán para disparar a las casillas del tablero del oponente.')
    print('El juego continúa hasta que todos los barcos de uno de los jugadores hayan sido hundidos.')
    print()

    # Crear tableros para ambos jugadores
    tablero_jugador_1 = Tablero()
    tablero_jugador_2 = Tablero()

    # Colocar barcos para el jugador 1
    colocar_barcos_jugador(tablero_jugador_1, 1)

    # Colocar barcos para el jugador 2
    colocar_barcos_jugador(tablero_jugador_2, 2)

    # Comenzar el juego
    jugador_actual = 1
    while True:
        if jugador_actual == 1:
            print('Turno del Jugador 1:')
            tablero_jugador_2.imprimir_tablero(oculto=True)
            print('Realiza un disparo:')
            pos_disparo = obtener_posicion_valida()
            resultado = tablero_jugador_2.recibir_disparo(pos_disparo[0], pos_disparo[1])
            print(resultado)
            print()
            if tablero_jugador_2.verificar_barco_hundido():
                print('¡Todos los barcos del Jugador 2 han sido hundidos!')
                print('¡El Jugador 1 es el ganador!')
                break
            jugador_actual = 2
        else:
            print('Turno del Jugador 2:')
            tablero_jugador_1.imprimir_tablero(oculto=True)
            print('Realiza un disparo:')
            pos_disparo = obtener_posicion_valida()
            resultado = tablero_jugador_1.recibir_disparo(pos_disparo[0], pos_disparo[1])
            print(resultado)
            print()
            if tablero_jugador_1.verificar_barco_hundido():
                print('¡Todos los barcos del Jugador 1 han sido hundidos!')
                print('¡El Jugador 2 es el ganador!')
                break
            jugador_actual = 1

# Iniciar el juego
jugar_batalla_naval()