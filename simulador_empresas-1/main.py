# filepath: c:\Users\elian\OneDrive - Universidad de Las Palmas de Gran Canaria\Curso 24-25 2do semestre\MNF\Trabajo MNF\Juego4Empresas\Juego4Empresas\simulador_empresas\main.py

import numpy as np
from utils import unodos, enteropos, positiva
from io_operations import load_old_game, save_game
from economia import calcular_costos, calcular_ingresos
from marketing import invertir_marketing

def main():
    print("\nJuego de empresas para cuatro participantes\n")
    print("¿Desea cargar una partida anterior o empezar otra?")
    print("1) Escriba 1 para cargar una partida antigua.")
    print("2) Escriba 2 para comenzar una partida nueva.")
    cargar = unodos()
    
    Empresa = ["Mercedes", "Peugeot", "Penhard-Levassor", "Mors"]
    
    if cargar == 1:
        game_data = load_old_game()
        UD = game_data['UD']
        V = game_data['V']
        Ventasreales = game_data['Ventasreales']
        VENTASPENDIENTES = game_data['VENTASPENDIENTES']
        PVP = game_data['PVP']
        CF = game_data['CF']
        CV = game_data['CV']
        STOCK = game_data['STOCK']
        CALM = game_data['CALM']
        CNOSERV = game_data['CNOSERV']
        CRUPT = game_data['CRUPT']
        INGRESOS = game_data['INGRESOS']
        CTOTAL = game_data['CTOTAL']
        PRESUPUESTO = game_data['PRESUPUESTO']
        CM = game_data['CM']
        Calm_arr = game_data['Calm']
        ruptadm = game_data['ruptadm']
        Crupt = game_data['Crupt']
        Cnoserv = game_data['Cnoserv']
        duracion = game_data['duracion']
    else:
        print("Introducción de los datos de partida")
        duracion = enteropos("Escriba la duración del juego en meses: ")
        
        UD = np.zeros((4, duracion+1), dtype=int)
        V = np.zeros((4, duracion+1), dtype=int)
        PVP = np.zeros((4, duracion+1))
        CV = np.zeros((4, duracion+1))
        CF = np.zeros((4, duracion+1), dtype=int)
        STOCK = np.zeros((4, duracion+1), dtype=int)
        INGRESOS = np.zeros((4, duracion+1))
        CTOTAL = np.zeros((4, duracion+1))
        CALM = np.zeros((4, duracion+1), dtype=int)
        Cnoserv = np.zeros((4, duracion+1), dtype=int)
        CRUPT = np.zeros((4, duracion+1), dtype=int)
        VENTASPENDIENTES = np.zeros((4, duracion+1), dtype=int)
        
        for i in range(4):
            PRESUPUESTO[i, 0] = positiva(f"Escriba la cantidad inicial de presupuesto disponible por la empresa {Empresa[i]}: ")
            PVP[i, 0] = positiva(f"Escriba el precio de venta al público inicial del producto de la empresa {Empresa[i]}: ")
            CF[i, 0] = positiva(f"Escriba el coste fijo de la empresa {Empresa[i]}: ")
            CV[i, 0] = positiva(f"Escriba el coste variable por cada unidad fabricada de la empresa {Empresa[i]}: ")
            CALM[i, 0] = positiva(f"Escriba el coste de almacenamiento por unidad de la empresa {Empresa[i]}: ")

        CM = np.full((4, 4), 0.25)

    for j in range(1, duracion+1):
        # Lógica del juego para cada mes
        pass  # Aquí se implementaría la lógica del juego

if __name__ == "__main__":
    main()