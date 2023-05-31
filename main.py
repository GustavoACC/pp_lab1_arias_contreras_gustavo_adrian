import re
from funciones import *

# Ruta del archivo con los datos de los jugadores y equipo
path_json_file = 'dt.json'

# Diccionario que se utilizara para generar el archivo csv del punto 3
datos_estadisticas_jugador = None

# Obtengo los valores del archivo
json_copy = obtener_valores_json(path_json_file)

# Main app
while True:
    imprimir_menu()
    opcion = input('\nIngrese la opción deseada: ')
    if not re.match(r'^[0-9]{1,2}', opcion):
        opcion = -1
    match(int(opcion)):
        case 1:
            imprimir_jugar_posicion(json_copy['jugadores'])
        case 2:
            datos_estadisticas_jugador = obtener_imprimir_estadisticas_jugador(
                json_copy['jugadores'])
        case 3:
            generar_csv_estadistica_jugador(datos_estadisticas_jugador)
        case 4:
            imprimir_logros_jugador(json_copy['jugadores'])
        case 5:
            imprimir_promedio_puntos_jugador(json_copy['jugadores'])
        case 6:
            imprimir_miembro_salon_fama(json_copy['jugadores'])
        case 7:
            imprimir_jugador_mayor_key(
                json_copy['jugadores'], 'rebotes_totales')
        case 8:
            imprimir_jugador_mayor_key(
                json_copy['jugadores'], 'porcentaje_tiros_de_campo')
        case 9:
            imprimir_jugador_mayor_key(
                json_copy['jugadores'], 'asistencias_totales')
        case 10:
            imprimir_jugador_supera_valor_clave_numerica(
                json_copy['jugadores'], 'promedio_puntos_por_partido')
        case 11:
            imprimir_jugador_supera_valor_clave_numerica(
                json_copy['jugadores'], 'rebotes_totales')
        case 12:
            imprimir_jugador_supera_valor_clave_numerica(
                json_copy['jugadores'], 'asistencias_totales')
        case 13:
            imprimir_jugador_mayor_key(
                json_copy['jugadores'], 'robos_totales')
        case 14:
            imprimir_jugador_mayor_key(
                json_copy['jugadores'], 'bloqueos_totales')
        case 15:
            imprimir_jugador_supera_valor_clave_numerica(
                json_copy['jugadores'], 'porcentaje_tiros_libres')
        case 16:
            imprimir_promedio_puntos_excluyendo_menor(json_copy['jugadores'])
        case 17:
            imprimir_jugador_mayor_logros(json_copy['jugadores'])
        case 18:
            imprimir_jugador_supera_valor_clave_numerica(
                json_copy['jugadores'], 'porcentaje_tiros_triples')
        case 19:
            imprimir_jugador_mayor_key(
                json_copy['jugadores'], 'temporadas')
        case 20:
            imprimir_jugadores_supera_valor_ordenados(json_copy['jugadores'])
        case 21:
            lista_estadisticas = [
                'puntos_totales', 'rebotes_totales', 'asistencias_totales', 'robos_totales']
            generar_csv_posiciones_estadisticas(
                json_copy['jugadores'], lista_estadisticas)
        case 22:
            imprimir_cantidad_jugadores_por_posicion(json_copy['jugadores'])
        case 23:
            imprimir_jugadores_por_cantidad_allstar(json_copy['jugadores'])
        case 24:
            imprimir_mejor_por_estadistica(json_copy['jugadores'])
        case 25:
            imprimir_mejor_jugador_total_estadisticas(json_copy['jugadores'])
        case 0:
            break
        case _:
            print('Ingreso una opción incorrecta')
