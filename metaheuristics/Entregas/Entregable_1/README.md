# Enunciado del problema: Diseño de un sistema de riego eficiente

## Autores: A.Badilla-Olivas, Brandon Mora, Gabriel Molina

Imagine que esta trabajando para una cooperativa agrícola, y se le ha asignado la tarea de diseñar un sistema de riego eficiente para un campo grande e irregularmente formado. El campo tiene diferentes condiciones del suelo y diferentes partes del campo necesitan diferentes cantidades de agua.

El problema es determinar el número y las posiciones óptimas de los aspersores para instalar, y cuánto tiempo debería funcionar cada uno, para minimizar el uso total de agua mientras se asegura que cada parte del campo recibe la cantidad necesaria de agua.

Este problema se puede abordar de manera adecuada utilizando el Whale Optimization Algorithm (WOA). Dada la naturaleza no lineal y multimodal del problema, un algoritmo de optimización global como el WOA podría utilizarse de manera efectiva. El algoritmo puede equilibrar entre la exploración (encontrar diferentes soluciones posibles) y la explotación (refinar las soluciones prometedoras), con el objetivo de lograr el objetivo de un uso eficiente del agua.

## Entendimiento del problema

En esta tarea, se tiene como objetivo diseñar un sistema de riego eficiente para un campo agrícola grande e irregularmente formado. El campo tiene diferentes condiciones del suelo, lo que significa que diferentes áreas requieren diferentes cantidades de agua.

## Componentes del problema

- Número de aspersores: Determinar el número óptimo de aspersores. Agregar más aspersores puede llevar a un riego más uniformemente distribuido, pero también significa costos más altos para la instalación y el mantenimiento.
- Posicionamiento de los aspersores: Determinar los mejores lugares para colocar los aspersores. El objetivo es asegurar una cobertura completa del campo mientras se evita la cobertura superpuesta, que desperdicia agua.
- Tiempo de operación: Determinar la cantidad de tiempo óptimo que cada aspersor debería operar. Diferentes áreas del campo podrían requerir diferentes cantidades de agua dependiendo de las condiciones del suelo y el tipo de cultivo, lo que significa que algunos aspersores pueden necesitar operar durante más tiempo que otros.
\end{enumerate

## Aplicación del Whale Optimization Algorithm

El Whale Optimization Algorithm (WOA) puede ayudar a encontrar la mejor solución a este problema. Las variables de decisión en este problema (es decir, el número, las posiciones y los tiempos de operación de los aspersores) se pueden codificar en un vector de solución, y el WOA se puede utilizar para buscar el vector de solución que minimiza el uso de agua mientras cumple con todos los requisitos de riego.

### Inicialización

El WOA comienza inicializando una población de posibles soluciones. En este caso, cada solución especificaría una cierta configuración de aspersores (es decir, su número, posiciones y tiempos de operación).

### Función objetivo

Esta es una función que calcula el uso total de agua de una solución dada, que buscamos minimizar. Tendría en cuenta la cantidad de agua que cada aspersor usa por unidad de tiempo, la cantidad de tiempo que opera cada aspersor, y la superposición entre las áreas cubiertas por diferentes aspersores.

### Exploración y Explotación

El WOA utiliza dos tipos de movimientos, rodeando a la presa y espiralando hacia la presa, para explorar y explotar el espacio de búsqueda. Los movimientos de rodeo ayudan a las ballenas a explorar una amplia gama de posibles soluciones, mientras que los movimientos en espiral les ayudan a converger hacia soluciones prometedoras.

### Mejora iterativa

El WOA actualiza continuamente sus soluciones en un intento de encontrar otras mejores. Utiliza la mejor solución encontrada hasta ahora como guía, y ajusta las otras soluciones para moverse hacia ella.

### Terminación

El algoritmo continúa hasta que se cumpla una condición de parada. Esto podría ser alcanzar un número máximo de iteraciones, o que las soluciones no mejoren significativamente durante un cierto número de iteraciones.

Al aplicar el WOA, podrías encontrar una configuración de riego eficiente y efectiva que ahorra agua y asegura que el campo esté bien regado.

## Heurística Voraz para el problema de riego

La heurística escogida para esta tarea es una que utiliza una táctica que explora el espacio de manera voraz, expandiendo de a pocos la solución. Aquí una breve explicación. 

### Inicialización

Se comienza colocando un solo aspersor en el centro del campo.

### Evaluación

Calcula el área total cubierta por el aspersor y la cantidad de agua utilizada. Además, evalúa si todas las áreas del campo están adecuadamente regadas.

### Elección Voraz

Si hay áreas que no están suficientemente regadas, añade otro aspersor en la ubicación que cubrirá el área adicional máxima que aún no está cubierta por los aspersores existentes.

### Iteración

Repite los pasos de evaluación y elección voraz hasta que todas las áreas del campo estén adecuadamente regadas.

### Optimización

Ajusta el tiempo de trabajo de cada aspersor en función de las necesidades de agua de su área de cobertura. Más tiempo para áreas con mayores necesidades de agua, y menos tiempo para áreas con menores necesidades de agua.

Esta heurística es simple y rápida, lo que la convierte en un buen enfoque inicial para el problema. Sin embargo, es posible que no proporcione la solución óptima ya que realiza elecciones óptimas locales en cada paso y no considera el óptimo global. Por ejemplo, podría terminar usando más aspersores de lo necesario porque añade aspersores tan pronto como encuentra un área que no está adecuadamente regada, en lugar de considerar una mejor configuración general de aspersores. El Algoritmo de Optimización de Ballenas (WOA), como algoritmo de optimización global, tendría más probabilidades de encontrar una mejor solución general.