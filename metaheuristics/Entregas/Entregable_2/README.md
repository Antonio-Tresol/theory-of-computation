# Enunciado del problema: Diseño de un sistema de riego eficiente

## Compilación y requisitos

Para compilar el programa se debe ejecutar el siguiente comando:

  cd Tarea2/Entregas/Entregable_2
  python3 main.py

Las librerías utilizadas en este programa son matplotlib.pyplot, time, numpy, math y random. Para instalarlas se debe ejecutar el siguiente comando:

  pip install matplotlib
  pip install numpy

## Autores: A.Badilla-Olivas, Brandon Mora, Gabriel Molina

Imagine que esta trabajando para una cooperativa agrícola, y se le ha asignado la tarea de diseñar un sistema de riego eficiente para un campo grande e irregularmente formado. El campo tiene diferentes condiciones del suelo y diferentes partes del campo necesitan diferentes cantidades de agua.

El problema es determinar el número y las posiciones óptimas de los aspersores para instalar, y cuánto tiempo debería funcionar cada uno, para minimizar el uso total de agua mientras se asegura que cada parte del campo recibe la cantidad necesaria de agua.

Este problema se puede abordar de manera adecuada utilizando el Whale Optimization Algorithm (WOA). Dada la naturaleza no lineal y multimodal del problema, un algoritmo de optimización global como el WOA podría utilizarse de manera efectiva. El algoritmo puede equilibrar entre la exploración (encontrar diferentes soluciones posibles) y la explotación (refinar las soluciones prometedoras), con el objetivo de lograr el objetivo de un uso eficiente del agua.

## Entendimiento del problema

En esta tarea, se tiene como objetivo diseñar un sistema de riego eficiente para un campo agrícola grande e irregularmente formado.
El campo tiene diferentes condiciones del suelo, lo que significa que diferentes áreas requieren diferentes cantidades de agua.

## Componentes del problema

- Número de aspersores: Determinar el número óptimo de aspersores. Agregar más aspersores puede llevar a un riego más uniformemente distribuido, pero también significa costos más altos gastos de agua.

- Posicionamiento de los aspersores: Determinar los mejores lugares para colocar los aspersores. El objetivo es asegurar una cobertura completa del campo mientras se evita la cobertura superpuesta, que desperdicia agua.

- Cobertura del terreno: dada una configuración de aspersores, determinar que tan bien se cubre el campo. El objetivo es asegurar que cada parte del campo reciba la cantidad necesaria de agua.

## Como se ven las soluciones del problema

una solución matrices nx3 donde cada fila es un vector con la posición del aspersor y el tipo [x, y, tipo] y donde n es el número de aspersores utilizados.

## Sobre los aspersores

- los aspersores tienen diferentes tipos 1, 2, 3, 4, 5
- cada tipo de aspersor tiene un uso de agua y un alcance diferente
- los aspersores tipos 1 llegan a los vecinos nivel 1 y dan a cada celda del terreno 20 de agua
- los aspersores tipos 2 llegan a los vecinos nivel 2 y dan a cada celda del terreno 14 de agua
- los aspersores tipos 3 llegan a los vecinos nivel 2 y dan a cada celda del terreno 16 de agua
- los aspersores tipos 4 llegan a los vecinos nivel 3 y dan a cada celda del terreno 13 de agua
- los aspersores tipos 5 llegan a los vecinos nivel 3 y dan a cada celda del terreno 12 de agua
Esto generala la función de uso de agua de un aspersor como:

## Función de uso de agua de un aspersor

Uso de agua = 180 \* aspersores_tipo_1 + 350 \* aspersores_tipo_2 + 400 \* aspersores_tipo_3 + 650 \* aspersores_tipo_4 + 800 \* aspersores_tipo_5

## Función de cobertura del terreno

Dada una matriz de terreno A de n x m y una matriz de aspersores S de n x m se irriga el terreno con respecto a cada aspersor (posicion y tipo) finalmente se calcula la cobertura del terreno como:
  
  for i : 0 in n:
      for j : 0 in m:
          cobertura = cobertura + abs(A[i][j])

## Actualización de la matriz de terreno

Dada una matriz de terreno A de n x m y una matriz de aspersores S de n x m
  
  for aspersor in s:
    regar_terreno(aspersor, A)

Donde regar_terreno es una función que recibe un aspersor y una matriz de terreno y actualiza la matriz de terreno con respecto a la posición y tipo del aspersor restandole a los vecinos del aspersor el agua que da el aspersor a cada celda a la que llega según su tipo.

## Función objetivo

Objetivo = alpha \* uso de agua + beta \* Cobertura del terreno

Donde alpha y beta son pesos que se le dan a cada función para determinar la importancia de cada una.

## Algoritmo de Fuerza Bruta para el problema de riego

  + La función "brute_force_algorithm" toma como entrada el terreno (terrain) y los aspersores disponibles (sprinklers). Se hace una copia del terreno original para comparar las soluciones viables más adealante.
  + La función interna "generate_sprinkler_combinations" se encarga de generar todas las combinaciones posibles de colocaciones de aspersores en el terreno.
  + Se verifica si no hay más aspersores disponibles. En ese caso, se genera una combinación vacía y se devuelve. De lo contrario, se selecciona el tipo de aspersor actual.
  + Se obtiene una copia de los aspersores restantes, excluyendo el tipo actual y se itera sobre cada posición en el terreno. Para cada posición, se itera sobre cada columna en el terreno.
  + Se crea un aspersor candidato, representado por una matriz de NumPy con las coordenadas de la posición y el tipo de aspersor.
  + Se verifica si el aspersor candidato es válido utilizando una función externa llamada "check_if_valid_sprinkler".
  + Se verifica si agregar el aspersor candidato a la solución actual mantiene una solución válida utilizando una función externa llamada "is_solution_valid".
  + Si el aspersor candidato es válido, se realiza una llamada recursiva a "generate_sprinkler_combinations" con los aspersores restantes y se itera sobre cada combinación generada.
  + Se devuelve la combinación actual junto con las combinaciones generadas en las llamadas recursivas.
  + Se itera sobre todas las combinaciones generadas por "generate_sprinkler_combinations".
  + En cada iteración, se calcula la aptitud de la combinación actual utilizando una función externa llamada "fitness_function".
  + Si la aptitud de la combinación actual es mejor que la mejor aptitud encontrada hasta el momento, se actualiza la mejor aptitud y se guarda la combinación como la mejor solución.
  + Finalmente, se devuelve la mejor solución encontrada como una matriz de coordenadas.

## Heurística Voraz para el problema de riego

El objetivo es determinar las posiciones y tipos óptimos de aspersores que se colocarán en un terreno dado.

El algoritmo toma dos entradas: terrain y sprinklers.

    terrain es una matriz 2D que representa el terreno donde se colocarán los aspersores.
    sprinklers es una matriz 1D que representa la cantidad de aspersores disponibles de cada tipo.

El algoritmo sigue estos pasos:

  + Inicializa una lista vacía solution para almacenar las posiciones y tipos de los aspersores colocados.
  + Establece la variable best_fitness en infinito para realizar un seguimiento del mejor valor de aptitud encontrado hasta el momento.
  + Crea una copia del terreno original.
  + Ingresa a un bucle que continúa hasta que no haya más colocaciones válidas de aspersores disponibles.
  + Itera sobre cada posición en el terreno y para cada posición, considera cada tipo de aspersor.
  + Verifica si la colocación del aspersor candidato es válida y si agregarlo a la solución mantiene una solución válida.
  + Si la colocación del aspersor candidato es válida, calcula su valor de aptitud.
  + Si el valor de aptitud es mejor que el mejor valor de aptitud actual, actualiza el mejor valor de aptitud y establece el aspersor candidato como el mejor aspersor.
  + Después de evaluar todos los aspersores candidatos posibles, si no se encuentra el mejor aspersor, sale del bucle.
  + De lo contrario, actualiza el terreno para reflejar la colocación del mejor aspersor.
  + Agrega el mejor aspersor a la lista de solución y reduce la cantidad de aspersores disponibles de ese tipo.
  + Repite los pasos 4 al 11 hasta que no haya más colocaciones válidas de aspersores.
  + Finalmente, devuelve la lista de solución.

## Solución con Whale Optimization Algorithm

El Whale Optimization Algorithm (WOA) puede ayudar a encontrar la mejor solución a este problema. Las variables de decisión en este problema (es decir, el número, las posiciones y los tipos del aspersor) se pueden codificar en un vector de solución, y el WOA se puede utilizar para buscar el vector de solución que minimiza el uso de agua mientras cumple con todos los requisitos de riego.

### Inicialización

El WOA comienza inicializando una población de posibles soluciones (search agents). En este caso, cada solución especificaría una cierta configuración de aspersores (una matriz, donde cada fila es un vector con la posion del aspersor y el tipo[x, y, tipo]).

Además necesitamos definir el número de iteraciones (número de generaciones) y el tamaño de la población (número de search agents). Estos parámetros se pueden ajustar para obtener un mejor rendimiento del algoritmo. También se puede ajustar el parámetro de peso de la función objetivo (alpha y beta) para determinar la importancia relativa de cada función. Finalmente, el WOA utiliza un parámetro de escala (a) para controlar la velocidad de convergencia del algoritmo y b y L para los movientos coordinados de red de burbujas.

### Exploración y Explotación

El WOA utiliza tres operadores para explorar y explotar el espacio de soluciones. Estos son: buscar, encirclar, atacar (red de burbujas).

Según las funciones de búsqueda, encirclar y atacar, el WOA actualiza las soluciones en cada iteración. Estas, definidas en el paper original de la metaheurística, funcionan con multiplicacion de vectores. Pues normalmente se trabaja con vectores de soluciones. Sin embargo dado que las soluciones en este problema son matrices, se debe adaptar la metaheurística ligeramente el algoritmo para que funcione con matrices.

Para ello, en vez de hacer las operadores correspondientes sobre la matriz directamente (lo que daría tamaños de matrices inconsistes conforme avanza el algoritmo) para actualizar la posición de un agente de busqueda (solucion) se actualizan individualmente las posiciones y tipo de cada aspersor de la solución. Así para cada operación necesaria del algoritmo.

En este proceso los asperores pueden salirse del terreno o tener un tipo no identificado. Se asume que cuando esto pasa el aspersor fue eliminado de la solución.

Cada iteración del algoritmo actualiza la posicion de las soluciones (search agents) y la mejor solución encontrada hasta el momento. Se ordenan las soluciones con respecto a que tan pequeño es es su resultado de la función objetivo (uso de agua + cobertura del terreno).El algorimo termina como con una lista ordenada de soluciones, la primera siendo la mejor encontrada al final de las iteraciones definidas.

## Comparación de resultados

Basándonos en los datos proporcionados, podemos extraer las siguientes conclusiones:

1. *Tiempo de ejecución*: El algoritmo codicioso es significativamente más rápido que el algoritmo WOA en todos los tamaños evaluados. El tiempo de ejecución del algoritmo codicioso es bastante bajo en comparación con el algoritmo WOA, lo que indica una mayor eficiencia en términos de velocidad de ejecución. El algoritmo de fuerza bruta apenas se podría comparar con el codicioso y realmente no tiene cabida en vista de lo ineficiente que es el calcular y comparar todas las soluciones candidatas posibles.

2. *Fitness*: El algoritmo WOA obtiene valores de fitness más altos en comparación con el algoritmo codicioso en todos los tamaños de terreno evaluados. También se utilizó en el algoritmo de fuerza bruta para mantener estándar de lectura para definir la mejor condición. Esto sugiere que el algoritmo WOA logra encontrar soluciones más óptimas en términos de la función objetivo utilizada.

3. *Cobertura de agua*: El algoritmo WOA muestra una mayor cobertura de agua en comparación con el algoritmo codicioso en la mayoría de los casos. Esto significa que el algoritmo WOA logra abarcar una mayor área del terreno con el suministro de agua disponible. Al igual que con el tiempo de ejecución, la cobertura abarcada no tiene cabida en el tiempo de prueba brindado para el algoritmo de fuerza bruta así que igualmente no es admisible en la comparación.

4. *Uso de agua*: El algoritmo codicioso muestra un menor uso de agua en comparación con el algoritmo WOA en la mayoría de los casos. Esto indica que el algoritmo codicioso logra utilizar el agua de manera más eficiente al evitar un exceso de riego. De la misma forma en la que la cobertura de agua no es admisible para el algoritmo de fuerza bruta, el uso de agua tampoco lo es.

En resumen, el algoritmo de fuerza bruta no puede resolver el problema en un rango de tiempo razonable así que no es viable utilizarlo en una solución del todo. El algoritmo WOA parece generar soluciones más óptimas en términos de fitness y cobertura de agua, pero a costa de un mayor tiempo de ejecución. Por otro lado, el algoritmo codicioso es más rápido y logra un uso más eficiente del agua, pero puede no alcanzar la misma calidad de solución que el algoritmo WOA. La elección del algoritmo a utilizar dependerá de la prioridad entre el tiempo de ejecución y la calidad de la solución deseada.
