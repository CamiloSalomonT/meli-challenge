# Desafío Teórico

## Procesos, hilos y corrutinas

### · Un caso en que usarías procesos para resolver un problema y por qué?
Para solucionar problemas de gran intesidad de procesamiento como multiplicaciones de matrices (en caso de no tener GPU), ordenamientos.

### · Un caso en que usarías threads para resolver un problema y por qué?
Para funcionamientos en paralelo de diferentes componentes de una aplicación, es decir, ejecutar diferentes comportamientos en cada thread.

### · Un caso en que usarías corrutinas para resolver un problema y por qué?
Cualquier problema que sea de mediana y gran escala, que sea extenuante en operaciones de I/O y no de procesamiento. Llamar páginas web, llamados masivos  aun API, escribir en una base de datos.


## Optimización de recursos del sistema operativo

### Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos información en una API HTTP. ¿Cómo lo harías? Explicar

##### Respuesta Corta: 
Realizaría una aplicación multi-task que me permitiera realizar las solicitudes de forma asíncrona (Como lo hice en el desafío técnico)

##### Respuesta Larga:
Primero experimentaría para ver que tantas request puedo en cortos periodos de tiempo hacer sin ser castigado (Esto debido a que los WAF protegen contra ataques DoS). De forma paralela, haría la investigación del peso promedio de las solicitudes, para revisar qué tanto podría meter en la memoria del computador. Con estos dos números podría calcular el número optimo de requests en paralelo que podría hacer al API, definiría lotes de ese tamaño para realizar las ejecuciones asíncronas al API en corrutinas, para utilizar mejor los recursos del sistema.
