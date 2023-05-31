import json
import re


def imprimir_menu():
    '''
    Imprime en consola las distintas opciones del menú según el documento propuesto
    No tiene parametros
    No retorna Valores
    '''
    print("\nMenú de opciones:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Mostrar estadisticas de un jugador")
    print("3. Guardar las estadisticas del jugador buscado en la opción 2 en un CSV")
    print("4. Buscar logros de un jugador por su nombre")
    print("5. Mostrar el promedio de puntos por partido del equipo")
    print("6. Buscar por nombre si un jugador es Miembro del Salón de la Fama del Baloncesto ")
    print("7. Mostrar el jugador con mayor cantidad de rebotes totales")
    print("8. Mostrar el jugador con mayor porcentaje de tiros de campo")
    print("9. Mostrar el jugador con mayor cantidad de asistencias totales")
    print("10. Mostrar jugadores que superen más puntos por partido según valor")
    print("11. Mostrar jugadores que superen más rebotes por partido según valor")
    print("12. Mostrar jugadores que superen más asistencias por partido según valor")
    print("13. Mostrar el jugador con mayor cantidad de robos totales")
    print("14. Mostrar el jugador con mayor cantidad de bloqueos totales")
    print("15. Mostrar jugadores que superen el porcentaje de tiros libres según valor")
    print("16. Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con menos cantidad")
    print("17. Mostrar el jugador con mayor cantidad de logros obtenidos")
    print("18. Mostrar jugadores que superen el porcentaje de tiros triples según valor")
    print("19. Mostrar el jugador con mayor cantidad de temporadas jugadas")
    print("20. Mostrar jugadores ordenados por posición que tengan un porcentaje de tiros de campo superior según valor")
    print("21. Bonus: Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking - Puntos, Rebotes, Asistencias, Robos")
    print("Opciones Extras:")
    print("22. Mostrar la cantidad de jugadores en cada posición")
    print("23. Mostrar la lista de jugadores ordenada por la cantidad de All-Star de forma descendente")
    print("24. Determinar que jugador tiene las mejores estadisticas en cada valor")
    print("25. Determinar que jugador tiene las mejores estadisticas de todos")
    print("0. Salir del programa")


def quick_sort_jugador_estadistica(lista_jugadores, key: str, ordenamiento: bool = True):
    '''
    En base a una lista de jugadores se realiza el ordenamiento de manera recursiva
    ascenciente o descendiente en base a la key enviada
    Parametros:
        lista_jugadores -> Lista de jugadores a ordenar que contiene estadisticas con un diccionario
        key -> Campo dentro del diccionario por el cual se ordenara
        ordenamiento -> se ordenara de manera ascendente (True) o descendiente (False)
    Devuelvo una lista ordenada
    '''
    if (len(lista_jugadores) <= 1):
        return lista_jugadores
    else:
        aux_lista_izq = []
        aux_lista_der = []
        pivote = lista_jugadores[0]
        for jugador in lista_jugadores[1:]:
            # True Ascendiente
            # False Descendiente
            if (ordenamiento):
                if (jugador['estadisticas'][key] < pivote['estadisticas'][key]):
                    aux_lista_izq.append(jugador)
                else:
                    aux_lista_der.append(jugador)
            else:
                if (jugador['estadisticas'][key] > pivote['estadisticas'][key]):
                    aux_lista_izq.append(jugador)
                else:
                    aux_lista_der.append(jugador)
        aux_lista_izq = quick_sort_jugador_estadistica(
            aux_lista_izq, key, ordenamiento)
        aux_lista_der = quick_sort_jugador_estadistica(
            aux_lista_der, key, ordenamiento)
        aux_lista_izq.append(pivote)
        aux_lista_izq += aux_lista_der
        return aux_lista_izq


def quick_sort_jugador_no_diccionario(lista_jugadores, key: str, ordenamiento: bool = True):
    '''
    En base a una lista de jugadores se realiza el ordenamiento de manera recursiva
    ascenciente o descendiente en base a la key enviada
    Parametros:
        lista_jugadores -> Lista de jugadores a ordenar que contiene estadisticas con un diccionario
        key -> Campo por el cual se ordenara que no sea un diccionario
        ordenamiento -> se ordenara de manera ascendente (True) o descendiente (False)
    Devuelvo una lista ordenada
    '''
    if (len(lista_jugadores) <= 1):
        return lista_jugadores
    else:
        aux_lista_izq = []
        aux_lista_der = []
        pivote = lista_jugadores[0]
        for jugador in lista_jugadores[1:]:
            # True Ascendiente
            # False Descendiente
            if (ordenamiento):
                if (jugador[key] < pivote[key]):
                    aux_lista_izq.append(jugador)
                else:
                    aux_lista_der.append(jugador)
            else:
                if (jugador[key] > pivote[key]):
                    aux_lista_izq.append(jugador)
                else:
                    aux_lista_der.append(jugador)
        aux_lista_izq = quick_sort_jugador_no_diccionario(
            aux_lista_izq, key, ordenamiento)
        aux_lista_der = quick_sort_jugador_no_diccionario(
            aux_lista_der, key, ordenamiento)
        aux_lista_izq.append(pivote)
        aux_lista_izq += aux_lista_der
        return aux_lista_izq


def generar_csv(archivo, nombre_archivo: str):
    '''
    Genera un archivo en base al los parametros enviados, no requiere que el nombre del archivo tenga la extension
    Parametros:
        archivo: Texto formateado para guardarse
        nombre_archivo: Nombre con el cual se guardara el archivo csv
    No retorna valores
    '''
    nombre_archivo = nombre_archivo + '.csv'
    with open(nombre_archivo, 'w+') as file:
        file.write(archivo)
        print('Se genero el archivo {0}'.format(nombre_archivo))


def imprimir_valor_referencia(valor: str, resultado, extra=None):
    '''
    Imprime en consola un valor principal y otro secundario separado por guion medio
    Parametros:
        valor: Valor que se desea mostrar como principal
        resultado: Valor que se desea ingresar como secundario
    No retorna valores
    '''
    if extra:
        print('{0} - {1} - {2}'.format(valor, resultado, extra))
    else:
        print('{0} - {1}'.format(valor, resultado))


def obtener_valores_json(json_file_name: str):
    '''
    Obtiene el listado completo de jugadres y otros datos que se encuentren en el json ingresado por path
    Parametros:
        json_file_name -> path completo de donde se encuentra el archivo json
    Retorna la variable global con los valores que se encuentran en el archivo json
    '''
    with open(json_file_name, 'r') as archivo:
        json_values = json.load(archivo)
        return json_values


def imprimir_jugar_posicion(lista_jugadores):
    '''
    Imprime los jugadores y su respectiva posicion en el equipo
    Parametros:
        lista_jugadores: Lista de los jugadores que se desea imprimir los datos
    No retorna valores
    '''
    for jugador in lista_jugadores:
        imprimir_valor_referencia(
            jugador['nombre'], jugador['posicion'])


def imprimir_jugares_indice(lista_jugadores):
    '''
    Imprime la lista de los jugadores y su indice para reconocer la posicion en las lista
    Parametros:
        lista_jugadores: Lista de jugadores a imprimir
    No retorno valores
    '''
    print('Lista de Jugares:')
    for index, jugador in enumerate(lista_jugadores):
        imprimir_valor_referencia(
            index, jugador['nombre'])


def obtener_imprimir_estadisticas_jugador(lista_jugadores):
    '''
    Imprime y retorna las estadisticas de un jugador ingresado por indice
    Parametros:
        lista_jugadores: Lista de la cual se realizara la busqueda según el indice ingresado
    Retorno un diccionario que posee el nombre del archivo a guardar y las estadisticas del jugador
    '''
    imprimir_jugares_indice(lista_jugadores)
    opcion = input(
        '\n Ingrese el indice del jugador que desea ver las estadisticas: ')
    # Valido el indice ingresado
    if not opcion.isnumeric():
        print('La opción ingresada debe ser numerica')
        return None
    if int(opcion) > (len(lista_jugadores)-1):
        print('La opción ingresada supera la cantidad de jugadores')
        return None
    lista_claves_csv = ['nombre', 'posicion']
    lista_valores_csv = [lista_jugadores[int(
        opcion)]['nombre'], lista_jugadores[int(opcion)]['posicion']]
    print('\nEstadisticas del jugador {0}:\n'.format(
        lista_jugadores[int(opcion)]['nombre']))

    # Guardo el nombre del archivo que usare en el csv del punto 3
    nombre_archivo_estadisticas = 'estadistidas_{0}'.format(
        lista_jugadores[int(opcion)]['nombre'].lower().replace(' ', '_'))
    for estadistica in lista_jugadores[int(opcion)]['estadisticas']:
        # Guardo los valores que necesito para el archivo csv de las estadisticas del punto 3
        lista_claves_csv.append(estadistica)
        lista_valores_csv.append(
            str(lista_jugadores[int(opcion)]['estadisticas'][estadistica]))
        imprimir_valor_referencia(
            estadistica, lista_jugadores[int(opcion)]['estadisticas'][estadistica])
    # Utilizo los join para tener las filas en los csv, en este caso con la coma como separador
    claves_csv = ",".join(lista_claves_csv)
    valores_csv = ",".join(lista_valores_csv)
    estadisticas_jugador = '{0}\n{1}'.format(claves_csv, valores_csv)
    return {
        'nombre_archivo': nombre_archivo_estadisticas,
        'valores_archivo': estadisticas_jugador
    }


def generar_csv_estadistica_jugador():
    '''
    Genero un archivo csv del jugador obtenido en el punto 2 solo si se busco previamente
    No requiere de parametros
    No retorna valores
    '''
    if datos_estadisticas_jugador:
        generar_csv(datos_estadisticas_jugador['valores_archivo'],
                    datos_estadisticas_jugador['nombre_archivo'])
    else:
        print('Aún no busco las estadisticas de un jugador')


def obtener_jugadores_por_nombre(lista_jugadores, nombre: str):
    '''
    Filtra y devuelve los jugadores que tengan el texto ingresado en su campo 'nombre'
    Parametros:
        lista_jugadores: Lista de jugadores en la cual se realizara la busqueda
        nombre: Texto por el cual se filtrara la lista de jugadores
    Retorna una Lista de Jugadores
    '''
    jugadores_encontrados = []
    for jugador in lista_jugadores:
        if re.search(nombre.lower(), jugador['nombre'].lower()):
            jugadores_encontrados.append(jugador)
    return jugadores_encontrados


def imprimir_logros_jugador(lista_jugadores):
    '''
    Imprime los logros del el o los jugadores encontrados según el texto ingresado
    Parametros:
        lista_jugadores: Lista de jugadores en la cual se realizara la busqueda
        nombre: Texto del cual se utilizara para buscar al jugador por el campo 'nombre' en la lista
    No retorna valores
    '''
    while True:
        buscar_nombre = input(
            'Ingrese el nombre el jugador que desea ver los logros: ')
        if not re.match(r'[^a-zA-Z\s]', buscar_nombre):
            print('Ingreso valores incorrectos intente nuevamente')
        else:
            break
    jugadores = obtener_jugadores_por_nombre(lista_jugadores, buscar_nombre)
    if len(jugadores) == 0:
        print('No se encontro algún jugador con ese nombre u apellido')
    else:
        print(jugadores)
        for jugador in jugadores:
            print('\n{0}'.format(jugador['nombre']))
            print('Logros: ')
            for logro in jugador['logros']:
                print('\t{0}'.format(logro))


def imprimir_miembro_salon_fama(lista_jugadores):
    '''
    Imprime si el o los jugadores encontrados son Miembros del Salón de la Fama del Baloncesto
    Parametros:
        lista_jugadores: Lista de jugadores en la que se realizara la busqueda
        nombre: Texto del cual se utilizara para buscar al jugador por el campo 'nombre' en la lista
    No retorna valores
    '''
    while True:
        buscar_nombre = input(
            'Ingrese el nombre el jugador que desea saber si es miembro: ')
        if re.match(r'[^a-zA-Z\s]', buscar_nombre):
            print('Ingreso valores incorrectos intente nuevamente')
        else:
            break
    jugadores = obtener_jugadores_por_nombre(lista_jugadores, buscar_nombre)
    patron = '^Miembro del Salon de la Fama del Baloncesto$'
    for jugador in jugadores:
        mensaje = 'El jugador {0} no es Miembro'.format(
            jugador['nombre'])
        for logro in jugador['logros']:
            if re.search(patron, logro):
                mensaje = 'El jugador {0} es Miembro del Salón de la Fama del Baloncesto'.format(
                    jugador['nombre'])
        print(mensaje)


def imprimir_jugador_mayor_key(lista_jugadores, key: str):
    '''
    Imprime el nombre y valor del jugador que tenga el mayor valor de la estadistica según clave
    Parametros:
        lista_jugadores: Lista en la que se buscara el jugador
        key: Clave de estadistica por la cual se quiere obtener el mayor
    No retorna valores
    '''
    resultado = quick_sort_jugador_estadistica(
        lista_jugadores, key, False)
    imprimir_valor_referencia(
        resultado[0]['nombre'], resultado[0]['estadisticas'][key])


def calcular_promedio_key_estadisticas(lista_jugadores, key: str):
    '''
    Calcula el promedio se una estadistica dentro de la lista de jugadores según la clave ingresada
    Parametros:
        lista_jugadores: La lista de jugadores de la cual se obtiene los datos para el calculo
        key: Clave por la cual se busca el valor en las estadisticas
    Retorna el promedio calculado
    '''
    suma_total = 0
    promedio = 0
    for jugador in lista_jugadores:
        suma_total += jugador['estadisticas'][key]
    promedio = suma_total / len(lista_jugadores)
    return promedio


def imprimir_jugador_mayor_logros(lista_jugadores):
    '''
    Imprime el jugador que tenga la mayor cantidad de logros según la lista ingresada
    Parametros:
        lista_jugadores: Lista de la cual se buscan los logros por jugador
    No retorna valores
    '''
    mayor_jugador = lista_jugadores[0]
    mayor_cantidad_logros = len(lista_jugadores[0]['logros'])
    lista_jugadores.pop(0)
    for jugador in lista_jugadores:
        if (len(jugador['logros']) > mayor_cantidad_logros):
            mayor_jugador = jugador
            mayor_cantidad_logros = len(jugador['logros'])
    imprimir_valor_referencia(
        mayor_jugador['nombre'], len(mayor_jugador['logros']))


def imprimir_jugador_supera_valor_clave_numerica(lista_jugadores, key: str, posicion=False):
    '''
    Imprime todos los jugadores de una lista ingresada que Superen el valor ingresado por teclado
    Parametros:
        lista_jugadores: Lista de los jugadores que seran analizados
        key: Clave de la cual se quiere imprimir los resultados
    No retorna valores
    '''
    encontro = False
    while True:
        buscar_valor = input('Ingrese el valor que desea buscar: ')
        if not re.match(r'^[0-9]+$|^[0-9]+\.[0-9]+$', buscar_valor):
            print('Ingreso un valor incorrecto, solo se permiten números, reintente')
        else:
            break
    buscar_valor = float(buscar_valor)
    for jugador in lista_jugadores:
        if jugador['estadisticas'][key] > buscar_valor:
            encontro = True
            if posicion:
                imprimir_valor_referencia(
                    jugador['nombre'], jugador['posicion'], jugador['estadisticas'][key])
            else:
                imprimir_valor_referencia(
                    jugador['nombre'], jugador['estadisticas'][key])
    if not encontro:
        print('No se encontraron jugadores que superen el valor indicado')


def imprimir_promedio_puntos_jugador(lista_jugadores):
    '''
    Imprime el promedio de puntos por partido de cada jugador de manera Ascendente
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
    No retorna valores
    '''
    resultado = quick_sort_jugador_estadistica(
        lista_jugadores, 'promedio_puntos_por_partido')
    for jugador in resultado:
        imprimir_valor_referencia(
            jugador['nombre'], jugador['estadisticas']['promedio_puntos_por_partido'])


def imprimir_promedio_puntos_excluyendo_menor(lista_jugadores):
    '''
    Imprime el promedio de puntos por partido excluyendo al que tiene menos puntos
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
    No retorna valores
    '''
    resultado = quick_sort_jugador_estadistica(
        lista_jugadores, 'promedio_puntos_por_partido')
    # Elimino de la lista al jugador con menor promedio de puntos por partido
    resultado.pop(0)
    promedio = calcular_promedio_key_estadisticas(
        resultado, 'promedio_puntos_por_partido')
    print('\nPromedio de puntos por partido: {0}\n'.format(promedio))


def imprimir_jugadores_supera_valor_ordenados(lista_jugadores):
    '''
    Imprime el promedio de puntos por partido excluyendo al que tiene menos puntos
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
    No retorna valores
    '''
    lista_ordenada = quick_sort_jugador_no_diccionario(
        lista_jugadores, 'posicion')
    imprimir_jugador_supera_valor_clave_numerica(
        lista_ordenada, 'porcentaje_tiros_de_campo', True)


def imprimir_cantidad_jugadores_por_posicion(lista_jugadores):
    '''
    Imprime en consola el total de jugadores de cada posicion
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
    No retorno valores
    '''
    posiciones = {}
    for jugador in lista_jugadores:
        if jugador['posicion'] in posiciones:
            posiciones[jugador['posicion']] += 1
        else:
            posiciones[jugador['posicion']] = 1
    posiciones_keys = posiciones.keys()
    for key in posiciones_keys:
        imprimir_valor_referencia(key, posiciones[key])


def imprimir_mejor_en_estadistica(lista_jugadores, key: str):
    '''
    Imprime el mejor jugador por la estadistica deseada y su valor
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
        key: Clave de la estadisctica por la cual se quiere obtener el mayor
    No retorno valores
    '''
    mensaje = 'Mayor cantidad de {0}'.format(key)
    lista_ordenada = quick_sort_jugador_estadistica(
        lista_jugadores, key, False)
    imprimir_valor_referencia(
        mensaje, lista_ordenada[0]['nombre'], lista_ordenada[0]['estadisticas'][key])


def imprimir_mejor_por_estadistica(lista_jugadores):
    '''
    Imprime un lista de los mejores jugadores por estadistica disponible
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
    No retorno valores
    '''
    # Obtengo el lista de las estadisticas disponibles
    estadisticas_keys = lista_jugadores[0]['estadisticas'].keys()
    for key in estadisticas_keys:
        imprimir_mejor_en_estadistica(lista_jugadores, key)


def imprimir_jugadores_por_cantidad_allstar(lista_jugadores):
    '''
    Imprime de forma descendiente los jugadores por cantidad de veces del logro de All-Star
    Parametros:
        lista_jugadores: Listado de jugadores del cual se obtendran los valores
    No retorna valores
    '''
    aux_lista_jugadores = []
    for jugador in lista_jugadores:
        # Agrego una flag en caso de no tener el logro
        encontrado = False
        for logro in jugador['logros']:
            if re.search(r'All-Star', logro):
                encontrado = True
                aux_allstar = logro.split(' ')
                aux_diccionario = {
                    'nombre': jugador['nombre'], 'allStar': logro, 'cantidad_allStar': int(aux_allstar[0])}
                aux_lista_jugadores.append(aux_diccionario)

        # En caso de no tener el logro se lo agrega como 0 para que no se pierda la cantidad total de jugadores
        if not encontrado:
            aux_diccionario = {
                'nombre': jugador['nombre'], 'allStar': '0 veces All-Star', 'cantidad_allStar': int(0)}
            aux_lista_jugadores.append(aux_diccionario)

    lista_ordenada = quick_sort_jugador_no_diccionario(
        aux_lista_jugadores, 'cantidad_allStar', False)
    for jugador in lista_ordenada:
        imprimir_valor_referencia(jugador['nombre'], jugador['allStar'])


def guardar_posicion_estadistica(lista_jugadores, lista_ordenada, key_estadisticas, key: str):
    '''
    Guarda valores en la lista referenciada en base a una lista previamente ordenada y la clave que se utilizo para ordenarla
    Parametros:
        lista_jugadores: Lista de jugadores donde se guardara el resultado final
        lista_ordenada: Lista de jugadores ordenada para obtener la posicion
        key_estadisticas: Clave donde se desea guardar dentro de la lista_jugadores el resultado
        key: Clave de la estadistica precisa a guardar su posicion de la lista ordenada
    No retorna valores
    '''
    for index, jugador_ordenado in enumerate(lista_ordenada):
        for jugador in lista_jugadores:
            if (jugador['nombre'] == jugador_ordenado['nombre']):
                jugador[key_estadisticas][key] = index + 1


def guardar_lista_posicion_estadistica_jugador(lista_jugadores, lista_diccionarios, key_estadisticas, lista_keys):
    '''
    Guarda valores dentro de a lista referenciada, ordenando y guardando la posicion en base a la lista de keys solicitada
    Parametros:
        lista_jugadores: Lista de jugadores donde se obtendran los valores
        lista_diccionarios: Lista donde se guardara por referencia el resultado final
        key_estadisticas: Clave que se utilizara para obtener las estadisticas de la lista de diccionarios
        lista_keys: Lista de Claves que se desean obtener las posiciones
    No retorna valores
    '''
    for jugador in lista_jugadores:
        aux_diccionario_inicial = {
            'nombre': jugador['nombre'], key_estadisticas: {}}
        lista_diccionarios.append(aux_diccionario_inicial)

    for key in lista_keys:
        aux_lista_ordenada = quick_sort_jugador_estadistica(
            lista_jugadores, key, False)
        guardar_posicion_estadistica(
            lista_diccionarios, aux_lista_ordenada, key_estadisticas, key)


def imprimir_mejor_jugador_total_estadisticas(lista_jugadores):
    '''
    Imprime en pantalla al jugador con mejores estadisticas dependiendo de su posicion general en todas las mismas
    Parametros:
        lista_jugadores: Lista de jugadores del cual se obtendran los valores
    No retorna valores
    '''
    aux_lista_diccionarios = []
    aux_keys = lista_jugadores[0]['estadisticas'].keys()
    guardar_lista_posicion_estadistica_jugador(
        lista_jugadores, aux_lista_diccionarios, 'posicion_estadisticas', aux_keys)

    aux_lista_totales = []
    for jugador in aux_lista_diccionarios:
        aux_total = 0
        for key in aux_keys:
            aux_total += jugador['posicion_estadisticas'][key]
        aux_diccionario_totales = {
            'nombre': jugador['nombre'], 'total_estadisticas': aux_total}
        aux_lista_totales.append(aux_diccionario_totales)
    total_ordenados = quick_sort_jugador_no_diccionario(
        aux_lista_totales, 'total_estadisticas')
    imprimir_valor_referencia(
        'El jugador con mayores estadisticas', total_ordenados[0]['nombre'])


def obtener_lista_posiciones_estadisticas_textual(jugador, lista_estadisticas):
    '''
    Devuelve una lista de strings con los valores dentro de las estadisticas solicitadas
    Parametros:
        jugador: Jugador del cual se obtienen los valores
        lista_estadisticas: Lista de claves con las estadisticas a guardar
    Retorna una lista de strings
    '''
    listado_resultados = []
    for estadistica in lista_estadisticas:
        listado_resultados.append(str(jugador['estadisticas'][estadistica]))
    return listado_resultados


def generar_csv_posiciones_estadisticas(lista_jugadores, lista_estadisticas):
    '''
    Genera un archivo Csv con la posicion en la que se registro de manera descendente en base a las claves de las estadisticas solicitadas
    Parametros:
        lista_jugadores: Lista de los jugadores de los cuales se obtienen los valores
        lista_estadisticas: Lista de claves que se desea obtener la posicion una vez ordenadas de forma Descendente
    No retorna valores
    '''
    aux_lista_diccionarios = []
    guardar_lista_posicion_estadistica_jugador(
        lista_jugadores, aux_lista_diccionarios, 'estadisticas', lista_estadisticas)
    aux_columnas = 'jugadores,{0}'.format(','.join(lista_estadisticas))
    aux_jugadores_columnas = ''
    for jugador in aux_lista_diccionarios:
        aux_estadisticas = obtener_lista_posiciones_estadisticas_textual(
            jugador, lista_estadisticas)
        print(aux_estadisticas)
        aux_jugador = '\n{0},{1}'.format(
            jugador['nombre'], ','.join(aux_estadisticas))
        aux_jugadores_columnas += aux_jugador
    archivo = '{0}{1}'.format(aux_columnas, aux_jugadores_columnas)
    generar_csv(archivo, 'posicion_estadisticas')
